#Word Vector Representation
#Name: Aayush Prasad @aprasad


import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "apple"
doc = nlp(text)

# Word vector representation
word_vector = doc.vector
print("Word Vector:", word_vector)