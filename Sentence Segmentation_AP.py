#Sentence Segmentation
#Name: Aayush Prasad @aprasad



import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "This is a sentence. This is another sentence."
doc = nlp(text)

# Sentence segmentation
for sent in doc.sents:
    print(sent.text)
