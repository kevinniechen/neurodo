import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems
import re


class GenSimBasics(object):
    def __init__(self):
        self.dictionary = None
        self.corpus = None
        self.words = None

class MyCorpus(object):
    def __init__(self, dictionary, words):
        self.dictionary = dictionary
        self.words = words
    def __iter__(self):
        for sentence in self.words:
            # assume there's one document per line, tokens separated by whitespace
            yield self.dictionary.doc2bow(sentence)
    def __len__(self):
        return len(self.words)

initializedItems = GenSimBasics()

def compute_basics():
    if initializedItems.corpus:
        return initializedItems

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # convert file to list of sentences, where sentences are split into words
    file = open('timecube_raw.txt')
    text = re.sub(r"""[^\w\s\.;!\?]""", '', file.read().lower())
    sentences = re.split(r'[\.!\?][ \n]', text)
    words = [sentence.split() for sentence in sentences]

    dictionary = corpora.Dictionary(sentence for sentence in words)
    corpus = MyCorpus(dictionary, words)

    initializedItems.words = words
    initializedItems.corpus = corpus
    initializedItems.dictionary = dictionary
    return initializedItems

def compute_corpus_and_dict():
    items = compute_basics()
    return items.corpus, items.dictionary
