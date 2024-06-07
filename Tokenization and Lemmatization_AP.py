#Tokenization and Lemmatization
#Name: Aayush Prasad @aprasad


import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)

# Tokenization
for token in doc:
    print(token.text)

# Lemmatization
for token in doc:
    print(token.text, token.lemma_)
