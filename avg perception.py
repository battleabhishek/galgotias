#chunking in nlp
import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')
from nltk import pos_tag,ragexphaser

grammer=r"""
np:{<DT/JN/NN:*>+}
PP:{}<IN><NP>
VP:{<VB:*><NP/PP/CLAUSE>+$}
clause:{<NP><VP>}
"""
TEXT="The quick brown fox jumps over the lazy dog"

words=word_tokenize(TEXT)
tagged_words=pos_tag(words)

grammer= r"""
NP:{<DT/JN/NN:*>+}
PP:{}<IN><NP>
VP:{<VB:*><NP/PP/CLAUSE>+$}
clause:{<NP><VP>}
""" 
parser=regex_parser(grammer)
chunked=parser.parse(tagged_words)
print(chunked)
chunked.pretty_print()