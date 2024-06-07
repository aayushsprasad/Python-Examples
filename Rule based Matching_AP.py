#Rule-based Matching
#Name: Aayush Prasad @aprasad


import spacy
from spacy.matcher import Matcher

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Initialize Matcher
matcher = Matcher(nlp.vocab)

# Define pattern
pattern = [{"LOWER": "hello"}, {"LOWER": "world"}]

# Add pattern to the matcher
matcher.add("HelloWorld", [pattern])

# Process text
text = "Hello World! Hello world!"
doc = nlp(text)

# Rule-based matching
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)