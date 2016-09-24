import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems
import re

initializedItems = {}

class MyCorpus(object):
    def __init__(self, dictionary, words):
        self.dictionary = dictionary
    def __iter__(self):
        for sentence in words:
            # assume there's one document per line, tokens separated by whitespace
            yield self.dictionary.doc2bow(sentence)

def compute_corpus_and_dict():
    if initializedItems.get("corpus") and initializedItems.get("dict"):
        return initializedItems["corpus"], initializedItems["dict"]

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # collect statistics about all tokens
    file = open('timecube_raw.txt')
    sentences = re.split('[\.!\?\n]', file.read().lower())


    words = [sentence.split() for sentence in sentences]
    dictionary = corpora.Dictionary(sentence for sentence in words)
    corpus = MyCorpus(dictionary, words)



    initializedItems["corpus"] = corpus
    initializedItems["dict"] = dictionary
    return corpus, dictionary
