#Text Classification
#Name: Aayush Prasad @aprasad



import spacy
from spacy.training import Example

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Text classification
text = "I love this product!"
example = Example.from_dict(doc=nlp(text), gold_dict={"cats": {"POSITIVE": 1.0}})
print(example)