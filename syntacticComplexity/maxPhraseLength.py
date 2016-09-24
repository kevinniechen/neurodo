


import nltk, re, pprint
import numpy as np

from collections import Counter
from nltk import word_tokenize


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def maxPhraseLength(filename):
    # filename = "/Users/williamshyr/Documents/MedHacks/cohere_proj/timecube_raw.txt"
    f = open(filename, 'r')
    raw = f.read()
    sentences = ie_preprocess(raw)
    grammar = "NP: {<DT|PP\$>?<JJ>*<NN>}"

    cp = nltk.RegexpParser(grammar)
    maxLen = 0
    for i in range(len(sentences)):
        result = cp.parse(sentences[i])
        for i in range(len(result)):
            if isinstance(result[i], nltk.tree.Tree):
                if len(result[i]) > maxLen:
                    maxLen = len(result[i])
    return maxLen
# return result


if __name__ == "__main__":
    filename = "/Users/williamshyr/Documents/MedHacks/cohere_proj/timecube_raw.txt"
    l = maxPhraseLength(filename)
    print(l)
