import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np

# Path to your document folder
folder_path = "path/to/your/documents"  

documents = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            documents.append(file.read())

print(f"Loaded {len(documents)} documents.")

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents).toarray()

index = faiss.IndexFlatL2(X.shape[1])
index.add(np.array(X, dtype=np.float32))

# Save the FAISS index and TF-IDF vectorizer
faiss.write_index(index, 'faiss_index.bin')
with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)

with open('documents.pkl', 'wb') as doc_file:
    pickle.dump({'documents': documents}, doc_file)
