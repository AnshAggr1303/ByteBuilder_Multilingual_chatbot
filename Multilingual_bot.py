from sentence_transformers import SentenceTransformer
import os
import numpy as np

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_text_files(text_folder):
    """
    Loads text files from the specified folder.
    """
    if not os.path.exists(text_folder):
        print(f"Error: Folder '{text_folder}' does not exist.")
        return []
        
    texts = []
    for filename in os.listdir(text_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(text_folder, filename), 'r', encoding='utf-8') as file:
                text = file.read().strip()
                if text:  # Skip empty files
                    texts.append(text)
                else:
                    print(f"Warning: {filename} is empty.")
    return texts

def vectorize_texts(texts):
    """
    Vectorizes the list of texts using SentenceTransformer.
    """
    return model.encode(texts, convert_to_numpy=True)

# Specify the folder where your text files are stored
text_folder = '/Users/anshagrawal/Desktop/quark_text'

# Load text files
texts = load_text_files(text_folder)

if texts:
    # Vectorize the texts
    vectors = vectorize_texts(texts)

    # Save the vectors and document texts
    np.save('document_vectors.npy', vectors)

    # Save document texts for reference during querying
    with open('document_texts.txt', 'w', encoding='utf-8') as f:
        for text in texts:
            f.write(text + '\n---DOCUMENT_SEPARATOR---\n')

    print("Text vectorization and saving complete!")
else:
    print("No valid texts found. Exiting.")

