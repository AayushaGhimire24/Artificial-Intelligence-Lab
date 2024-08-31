import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Example text
text = "Hello! How are you? I hope you are doing well."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for sentence in sentences:
    print(sentence)
print()

# Word Tokenization
sentence = "This is an example sentence."
words = word_tokenize(sentence)
print("Word Tokenization:")
for word in words:
    print(word)
print()

# Stop Words Filtering
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.casefold() not in stop_words]
print("Stop Words Filtering:")
for word in filtered_words:
    print(word)
print()

# Word Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("Word Stemming:")
for word in stemmed_words:
    print(word)
print()

# POS Tagging
pos_tags = pos_tag(words)
print("POS Tagging:")
for word, tag in pos_tags:
    print(word, tag)
print()