import os
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np
import pickle

# Define the folder path containing the text files (update this to your directory)
folder_path = "/Users/anshagrawal/Desktop/quark_text"

# Read all text files in the folder and store their contents in a list
documents = []
filenames = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Assuming your documents are .txt files
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            documents.append(file.read())
            filenames.append(filename)

print(f"Loaded {len(documents)} documents.")

# Initialize the TF-IDF Vectorizer and convert documents into vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents).toarray()

print(f"TF-IDF matrix shape: {X.shape}")  # Shape: (num_docs, num_features)

# Initialize FAISS index (using L2 distance metric)
index = faiss.IndexFlatL2(X.shape[1])
index.add(np.array(X, dtype=np.float32))  # Add vectors to FAISS index

print("FAISS index created and documents indexed.")

# Save the FAISS index and vectorizer for future searches
faiss.write_index(index, "faiss_index.bin")
with open("tfidf_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)
with open("documents.pkl", "wb") as doc_file:
    pickle.dump({"documents": documents, "filenames": filenames}, doc_file)

print("FAISS index, vectorizer, and documents saved.")
