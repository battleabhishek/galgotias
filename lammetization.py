#lemmetiztion in nlp 
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('wordnet')

def lemmatize_sentence(sentence):
    lemmatizer = nltk.WordNetLemmatizer()
    words = word_tokenize(sentence)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

text ="the cat are chasing mice and playing in the garden"
text ="the cat are running and eating fishes"
print(lemmatize_sentence(text))
