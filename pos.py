#pos tagging
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "I am learning Natural Language Processing."
words = word_tokenize(sentence)
taagged_words = nltk.pos_tag(words)
print(taagged_words)

#(nlp,nnp)
def pos_tagging(text):
    word = word_tokenize(text)
    tagged_words = nltk.pos_tag(word)
    return tagged_words

text = "I am learning Natural Language Processing."
result = pos_tagging(text)
print(result)
