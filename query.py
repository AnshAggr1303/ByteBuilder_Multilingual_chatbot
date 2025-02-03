import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Load the FAISS index
index = faiss.read_index('/Users/anshagrawal/Desktop/quark_/document_index.index')  # Correct path

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to load .txt files into a list
def load_texts_from_files(txt_folder):
    texts = []
    for filename in os.listdir(txt_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(txt_folder, filename)
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
            texts.append(text)
    return texts

# Replace 'your_txt_folder' with the actual folder containing your .txt files
txt_folder_path = '/Users/anshagrawal/Desktop/quark_text'  # Correct this path
texts = load_texts_from_files(txt_folder_path)

# Query function
def query_index(query):
    query_vector = model.encode([query], convert_to_numpy=True)
    k = 5  # Number of top results to retrieve
    distances, indices = index.search(query_vector, k)

    print(f"Top {k} results for query '{query}':")
    for i in range(k):
        doc_index = indices[0][i]
        print(f"{i+1}. Document {doc_index + 1} with distance {distances[0][i]}")
        print(f"   Content: {texts[doc_index][:500]}...")  # Preview the first 500 characters of the document
        print()

# Test the query
query = input("Enter a search query: ")
query_index(query)