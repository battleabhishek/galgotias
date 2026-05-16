#breaking of text "this is class of nlp"."this is intresting"
text = "this is class of nlp. this is intresting"
#tokenization
tokens = text.split()
print(tokens)
#words
words = [token for token in tokens if token.isalpha()]
print("Words:", words)
#sentences
sentences = text.split('.')
print("Sentences:", sentences)
#twitter like tokenization
import re
twitter_text = "Hello @user, check out #NLP! Visit https://example.com"
twitter_tokens = re.findall(r'@\w+|#\w+|https?://\S+|\w+', twitter_text)
print("Twitter Tokens:", twitter_tokens)
#rager tokenization
rager_text = "This is an example of rager tokenization."
rager_tokens = re.findall(r'\b\w+\b', rager_text)

print(word_tokenize(text))

def word_tokenize(text):
    sentences = text.split(text)
    word_tokens =sent_tokenize(text)
    return sentence_tokens, word_tokens
    