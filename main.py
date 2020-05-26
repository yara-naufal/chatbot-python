import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import warnings
warnings.filterwarnings("ignore")

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        extractedWords = nltk.word_tokenize(pattern)
        words.extend(extractedWords)
        docs_x.append(pattern)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])