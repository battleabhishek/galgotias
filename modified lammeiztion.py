#modified lemmetiztion in nlp 
import nltk
from nltk.tokenize import word_tokenize
from ntlk.stem import WordNetLemmatizer
from ntlk.corpus import wordnet 
nltk.download('punkt_tab')
nltk.download('wordnet')
ntlk.download('')
ntlk.download
ntlk.download

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    


def lemmatize_sentence(sentence):
    lemmatizer = nltk.WordNetLemmatizer()
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) 
                        for word, tag in pos_tags]
    return ' '.join(lemmatized_words)

text ="the cat are chasing mice and playing in the garden"
text ="the cat are running and eating fishes"
text = "the stripped bat are hannging on their feet for best "
print(lemmatize_sentence(text))
