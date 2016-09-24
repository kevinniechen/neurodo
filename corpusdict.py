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

def compute_basics(file_name):
    text = ''
    with open(file_name) as file:
        text = file.read()
    return compute_basics_text(text)

def compute_basics_text(text):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # convert file to list of sentences, where sentences are split into words
    text = re.sub(r"""[^\w\s\.;!\?]""", '', text.lower())
    sentences = re.split(r'[\.!\?][ \n]', text)
    words = [sentence.split() for sentence in sentences]

    dictionary = corpora.Dictionary(sentence for sentence in words)
    corpus = MyCorpus(dictionary, words)

    initialized_items = GenSimBasics()
    initialized_items.words = words
    initialized_items.corpus = corpus
    initialized_items.dictionary = dictionary
    return initialized_items
