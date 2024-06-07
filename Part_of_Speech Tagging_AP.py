#Part-of-Speech Tagging
#Name: Aayush Prasad @aprasad



import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)

# Part-of-speech tagging
for token in doc:
    print(token.text, token.pos_)