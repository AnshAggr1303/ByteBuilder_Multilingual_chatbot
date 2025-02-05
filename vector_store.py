import faiss
import numpy as np
import pickle

class FaissVectorDB:
    def __init__(self, index_path, vectorizer_path, documents_path):
        self.index = faiss.read_index(index_path)

        with open(vectorizer_path, 'rb') as vec_file:
            self.vectorizer = pickle.load(vec_file)

        with open(documents_path, 'rb') as doc_file:
            document_data = pickle.load(doc_file)
            self.documents = document_data['documents']

    def search(self, query, top_k=3):
        query_vector = self.vectorizer.transform([query]).toarray().astype(np.float32)
        distances, indices = self.index.search(query_vector, top_k)
        return [self.documents[i] for i in indices[0]]
