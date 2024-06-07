#Text Similarity
#Name: Aayush Prasad @aprasad


import spacy

# Load a larger spaCy model with word vectors
nlp = spacy.load("en_core_web_md")

# Now compute similarity between documents
doc1 = nlp("This is a sample document.")
doc2 = nlp("This is another document.")

# Text similarity
similarity = doc1.similarity(doc2)
print("Similarity:", similarity)