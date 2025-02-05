import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from translator import detect_language, translate_to_english, translate_to_hindi
from bloom_response import BloomLLM
from vector_store import FaissVectorDB
import pickle

# Initialize Bloom LLM
bloom = BloomLLM()

# Load the FAISS index, TF-IDF vectorizer, and documents
faiss_db = FaissVectorDB('faiss_index.bin', 'tfidf_vectorizer.pkl', 'documents.pkl')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your health assistant bot. Ask me any health-related questions.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text

        # Step 1: Detect language and translate if necessary
        detected_lang = detect_language(user_input)
        english_input = translate_to_english(user_input)

        # Step 2: Perform FAISS-based document retrieval
        relevant_docs = faiss_db.search(english_input)

        # Step 3: Clean and prepare the context for Bloom
        context_text = " ".join(relevant_docs[:2])[:1000]  # Limit to 1000 characters

        # Step 4: Generate response using Bloom LLM
        prompt = f"Context: {context_text}\n\nUser: {english_input}\nResponse:"
        bloom_response = bloom.generate_response(prompt, max_new_tokens=80)

        # Step 5: Translate response back to the original language
        final_response = translate_to_hindi(bloom_response, detected_lang)

        # Step 6: Send the response to the user
        await update.message.reply_text(final_response)

    except Exception as e:
        await update.message.reply_text("Sorry, an error occurred while processing your query.")
        print(f"Error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token('YOUR_TELEGRAM_BOT_TOKEN').build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
