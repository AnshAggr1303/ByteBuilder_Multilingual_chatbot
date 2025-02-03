import os

def load_texts_from_files(txt_folder):
    """
    Loads text content from all .txt files in the given folder.
    """
    texts = []
    
    # Iterate through all .txt files in the given folder
    for filename in os.listdir(txt_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(txt_folder, filename)
            
            # Open the .txt file and read the content
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
                
                # Add the extracted text to the list
                texts.append(text)
    
    return texts

# Replace 'your_txt_folder' with the actual folder containing your .txt files
txt_folder_path = '/Users/anshagrawal/Desktop/quark_text'
texts = load_texts_from_files(txt_folder_path)

# Now you can use the 'texts' list for your FAISS search
print(f"Loaded {len(texts)} documents.")