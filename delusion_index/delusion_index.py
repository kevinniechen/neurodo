import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems
from corpusdict import compute_basics

basics = compute_basics()
dictionary = basics.dictionary
corpus = basics.corpus
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(basics.words))
doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
#vec_lsi = lsi[vec_bow] # convert the query to LSI space
#print(vec_lsi)
