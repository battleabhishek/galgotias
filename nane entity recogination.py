#name entity recogination
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')  
nltk.download('words')

def named_entity_recognition(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    return named_entities
text = "Apple Inc. is a technology company based in Cupertino, California."
entities = named_entity_recognition(text)
print(entities)


