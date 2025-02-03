import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Load the FAISS index
index = faiss.read_index('/Users/anshagrawal/Desktop/quark_/document_index.index')  # Replace with your index path

# Initialize the Sentence-Transformer model
model_st = SentenceTransformer('all-MiniLM-L6-v2')

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Set pad_token to eos_token, as GPT-2 does not have a pad token by default
tokenizer.pad_token = tokenizer.eos_token

gpt2_model = GPT2LMHeadModel.from_pretrained('gpt2')
gpt2_model.eval()

# Load .txt files into the texts list
def load_texts_from_files(txt_folder):
    texts = []
    for filename in os.listdir(txt_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(txt_folder, filename)
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
            texts.append(text)
    return texts

# Replace with your folder containing .txt files
txt_folder_path = '/Users/anshagrawal/Desktop/quark_text'
texts = load_texts_from_files(txt_folder_path)

# Function to query FAISS index and get most similar documents
def query_index(query):
    query_vector = model_st.encode([query], convert_to_numpy=True)
    k = 5  # Number of top results to retrieve
    distances, indices = index.search(query_vector, k)
    
    # Collect top-k document content
    retrieved_docs = []
    for i in range(k):
        doc_index = indices[0][i]
        retrieved_docs.append(texts[doc_index][:500])  # Preview the first 500 characters of each document
    return " ".join(retrieved_docs)  # Combine the retrieved documents into one string

# Function to generate a response with GPT-2
def generate_gpt2_response(query):
    # Get the context from FAISS query
    context = query_index(query)
    
    # Prepare the prompt by adding the context
    prompt = f"Here are some documents related to your query:\n{context}\n\nBased on these documents, here's what I found:"
    
    # Tokenize the input and create an attention mask
    inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=1024, padding=True)
    attention_mask = (inputs != tokenizer.pad_token_id).type(inputs.dtype)  # Create attention mask
    
    # Generate the response with no repeated n-grams and a limited output length
    with torch.no_grad():
        outputs = gpt2_model.generate(inputs, attention_mask=attention_mask, max_new_tokens=200, num_return_sequences=1, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)
    
    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Test the system by querying
query = input("Enter a search query: ")
response = generate_gpt2_response(query)
print("\nGPT-2 Response:")
print(response)
