#Named Entity Recognition
#Name: Aayush Prasad @aprasad


import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(text)

# Named entity recognition
for ent in doc.ents:
    print(ent.text, ent.label_)