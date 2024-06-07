#Custom Named Entity Recognition
#Name: Aayush Prasad @aprasad
import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Define patterns for custom named entities
patterns = [
    [{"LOWER": "apple"}],  # Note: Removed the "label" key from each dictionary
]

# Add patterns to the matcher
matcher = spacy.matcher.Matcher(nlp.vocab)
matcher.add("CUSTOM_NER", patterns)

# Process text
text = "Apple announces new iPhone 13."
doc = nlp(text)

# Custom named entity recognition
matches = matcher(doc)
for match_id, start, end in matches:
    entity = doc[start:end]
    print(entity.text, entity.label_)
