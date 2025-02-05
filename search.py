import faiss
import numpy as np
import pickle

# Load the saved FAISS index, vectorizer, and documents
index = faiss.read_index("faiss_index.bin")

with open("tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

with open("documents.pkl", "rb") as doc_file:
    data = pickle.load(doc_file)
    documents = data["documents"]
    filenames = data["filenames"]

def search_documents(query, index, vectorizer, top_k=3):
    """
    Search for the top K most relevant documents using FAISS.
    :param query: User's search query
    :param index: FAISS index
    :param vectorizer: TF-IDF vectorizer
    :param top_k: Number of top results to return
    :return: List of top documents and corresponding filenames
    """
    # Convert the query to a TF-IDF vector
    query_vec = vectorizer.transform([query]).toarray().astype(np.float32)

    # Perform the search
    distances, indices = index.search(query_vec, k=top_k)

    # Get the top matching documents and their filenames
    results = [(documents[i], filenames[i]) for i in indices[0]]

    return results

# Example search query
query = "lic life insurance?"
results = search_documents(query, index, vectorizer)

print("Top retrieved documents:")
for idx, (doc, filename) in enumerate(results, 1):
    print(f"\nDocument {idx} (from file: {filename}):\n{doc[:500]}...")
