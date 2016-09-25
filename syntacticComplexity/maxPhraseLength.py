


import nltk, re, pprint
import numpy as np

from collections import Counter
from nltk import word_tokenize


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def max_phrase_length_text(raw_text):
    sentences = ie_preprocess(raw_text)
    grammar = """
    VP: {<DT>?<JJ>*<PRP>?<NN>?<MD>?<VB|VBD|VBP|VBG|VBZ|VBN>?<IN>?<DT>?<JJ>*<NN>}"""
    # grammar = """
    #     VP: {<DT>?<PRP>?<MD>?<VB>?<JJ>*<NN>}"""
    # grammar = "NP: {<DT|PP>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    maxLen = 0
    for i in range(len(sentences)):
        result = cp.parse(sentences[i])
        for tree in result:
            if isinstance(tree, nltk.tree.Tree):
                if len(tree) > maxLen:
                    maxLen = len(tree)
                    maxNode = tree
                    maxSent = sentences[i]
                    sentIndex = i
    return maxLen

"""
maxPhraseLength is the function that gives the maximum phrase length of the text.
"""
def maxPhraseLength(filename):
    with open(filename, 'r') as f:
        return max_phrase_length_text(f.read())
    return 0



if __name__ == "__main__":
    # filename = "/Users/williamshyr/Documents/MedHacks/cohere_proj/timecube_raw.txt"
    filename = "/Users/williamshyr/Documents/MedHacks/cohere_proj/syntacticComplexity/testPhraseLength.txt"
    l = maxPhraseLength(filename)
    print(l)
