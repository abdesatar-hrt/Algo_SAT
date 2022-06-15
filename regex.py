import nltk
from nltk.tokenize import word_tokenize

text = "Hi Mr.s Smith! i'm going to shopping would you like me to buy sime vegetables. For our dinner today it's goona be pretty good."
word_tokenizer = word_tokenize(text)

for word in word_tokenizer:
    print(word)