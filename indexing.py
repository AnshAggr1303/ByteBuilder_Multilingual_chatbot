
import faiss
import numpy as np

# Load the document vectors (make sure this is the correct path and file format)
vectors = np.load('/Users/anshagrawal/Desktop/quark_/document_vectors.npy', allow_pickle=True)  # Ensure this is a .npy file

# Convert vectors to float32 if they are not already
vectors = vectors.astype(np.float32)

# Ensure the vectors have the correct dimensions (typically 384 for 'all-MiniLM-L6-v2')
print(vectors.shape)  # Make sure the shape is [num_vectors, 384]

dim = vectors.shape[1]  # Dimension of the vectors

# Create the FAISS index (using a flat index in this case)
index = faiss.IndexFlatL2(dim)  # For L2 distance (Euclidean)

# Add the vectors to the index
index.add(vectors)

# Save the FAISS index to a file (optional, to load it later)
faiss.write_index(index, '/Users/anshagrawal/Desktop/quark_/document_index.index')

print("FAISS index has been created and saved!")
