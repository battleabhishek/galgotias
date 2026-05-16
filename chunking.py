#chunking in nlp
import nltk 
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('words')
def chunk_sentence(sentence):
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    chunked = nltk.ne_chunk(pos_tags)
    return chunked

text = "Apple is looking at buying U.K. startup for $1 billion"
print(chunk_sentence(text))
