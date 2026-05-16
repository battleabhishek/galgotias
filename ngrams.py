# n gram in nlp
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')

text = "i love natural language processing"
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    n_grams = ngrams(tokens, n)
    return list(n_grams)
text = "Natural language processing is a fascinating field."
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)

for i in range(1, 4):
    n_grams = generate_ngrams(text, i)
    print(f"{i}-grams:", n_grams)



