import faiss
import numpy as np

class FaissVectorDB:
    def __init__(self, faiss_index_path, vectorizer, documents):
        """
        Initialize the FAISS vector database.
        :param faiss_index_path: Path to the saved FAISS index file.
        :param vectorizer: The TF-IDF vectorizer for embedding queries.
        :param documents: The list of documents corresponding to the FAISS index.
        """
        self.index = faiss.read_index(faiss_index_path)
        self.vectorizer = vectorizer
        self.documents = documents

    def search(self, query, top_k=3):
        """
        Search the FAISS index and return the top-k relevant documents.
        :param query: The user query string.
        :param top_k: Number of top results to return.
        :return: A list of top-k relevant documents.
        """
        # Convert the query to a TF-IDF vector
        query_vector = self.vectorizer.transform([query]).toarray().astype(np.float32)

        # Perform the search
        distances, indices = self.index.search(query_vector, top_k)

        # Retrieve the top documents
        top_documents = [self.documents[i] for i in indices[0]]
        return top_documents

    def add_new_documents(self, new_documents, vectorizer):
        """
        Dynamically add new documents to the FAISS index.
        :param new_documents: A list of new documents to index.
        :param vectorizer: The TF-IDF vectorizer for embedding the new documents.
        """
        # Vectorize the new documents
        new_vectors = vectorizer.transform(new_documents).toarray().astype(np.float32)

        # Add the new vectors to the FAISS index
        self.index.add(new_vectors)

        # Update the internal document list
        self.documents.extend(new_documents)
