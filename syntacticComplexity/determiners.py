# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:49:44 2016

@author: williamshyr
"""

import nltk, re, pprint

from collections import Counter
from nltk import word_tokenize
import numpy as np

def determinersCount(filename):
    f = open(filename, 'r')
    raw = f.read()
    # tokenization
    tokens = word_tokenize(raw)
    # print(tokens[1:10])
    text = nltk.Text(tokens)
    # print(text[1:10])
    # print(type(tokens))
    # print(type(text))
    tagged = nltk.pos_tag(text)
    counts = Counter(tag for word, tag in tagged)
    # print(counts)
    deter = ["DT", "WDT"]
    return dict(zip(deter, [counts["DT"], counts["WDT"]]))


def determiners(filenmae):
    deter = ["that", "what", "whatever", "which", "whichever"]
    f = open(filename, 'r')
    raw = f.read()
    # tokenization
    tokens = word_tokenize(raw)
    # print(tokens[1:10])
    text = nltk.Text(tokens)
    # print(text[1:10])
    # print(type(tokens))
    # print(type(text))
    numDeter = np.zeros(len(deter))
    for i in range(len(deter)):
        numDeter[i] = text.count(deter[i])
    deterDict = dict(zip(deter, numDeter))
    return deterDict

if __name__ == "__main__":
    filename = "/Users/williamshyr/Documents/MedHacks/cohere_proj/timecube_raw.txt"
    c = determinersCount(filename)
    print(c)
    n = determiners(filename)
    print(n)
