import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from translator import detect_language, translate_to_english, translate_to_hindi
from bloom_response import BloomLLM
import faiss
import numpy as np
import pickle

# Initialize Bloom LLM
bloom = BloomLLM()

# Load the FAISS index, vectorizer, and documents
faiss_index = faiss.read_index('/Users/anshagrawal/Desktop/Quark_final/faiss_index.bin')

with open('/Users/anshagrawal/Desktop/Quark_final/tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

with open('/Users/anshagrawal/Desktop/Quark_final/documents.pkl', 'rb') as doc_file:
    document_data = pickle.load(doc_file)
    documents = document_data['documents']
    filenames = document_data['filenames']

def search_documents(query, index, vectorizer, top_k=2):
    # Convert query into TF-IDF vector
    query_vec = vectorizer.transform([query]).toarray().astype(np.float32)
    
    # Perform FAISS search
    distances, indices = index.search(query_vec, top_k)
    
    # Retrieve top documents
    results = [documents[i] for i in indices[0]]
    return results

def clean_context(relevant_docs):
    """
    Clean and limit the context length.
    """
    combined_context = " ".join(relevant_docs[:2])[:800]  # Limit to 800 characters for better response control
    cleaned_context = " ".join(combined_context.split())  # Remove extra spaces and line breaks
    return cleaned_context

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your multilingual chatbot powered by TF-IDF and Bloom.\n"
                                    "You can ask me any health-related question.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text

        # Step 1: Detect language and translate input if necessary
        detected_lang = detect_language(user_input)
        english_input = translate_to_english(user_input)

        # Step 2: Perform FAISS-based document retrieval
        relevant_docs = search_documents(english_input, faiss_index, vectorizer)

        # Step 3: Clean and limit the context before passing it to Bloom
        context_text = clean_context(relevant_docs)

        # Step 4: Generate response using Bloom LLM with better randomness settings to avoid repetition
        prompt = f"{context_text}\n\n{english_input}\n"
        bloom_response = bloom.generate_response(prompt, max_new_tokens=80)

        # Step 5: Clean and fix repetitive text (post-processing)
        bloom_response = fix_repetitive_text(bloom_response)

        # Step 6: Translate response back to the original language
        final_response = translate_to_hindi(bloom_response, detected_lang)

        # Step 7: Send response to user
        await update.message.reply_text(final_response)

    except Exception as e:
        # Handle any errors and log them for debugging
        await update.message.reply_text("An error occurred while processing your request. Please try again.")
        print(f"Error: {e}")

def fix_repetitive_text(response):
    """
    Fix repetitive phrases and trim long responses.
    """
    # Split the response into sentences and remove duplicates
    seen = set()
    sentences = []
    for sentence in response.split(". "):
        sentence = sentence.strip()
        if sentence not in seen:
            seen.add(sentence)
            sentences.append(sentence)

    # Rejoin the cleaned sentences and limit the output length
    cleaned_response = ". ".join(sentences)[:300]  # Limit to 300 characters
    return cleaned_response.strip()

if __name__ == "__main__":
    app = ApplicationBuilder().token('7807860814:AAGdHtg0EyNWozx8HcKANHjPMCmVlHyoUlc').build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
