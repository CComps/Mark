import json
import nltk
from nltk.stem import *

lmt = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',', ':', ';', '-', '_', '*', '#', '@', '$', '%', '^', '&', '+', '=', '~', '`', '{', '}',
                '|', '\\', '<', '>', '"', "'", '(', ')', '[', ']', '\n', '\t', '\r']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


print(documents)
