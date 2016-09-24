import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems
from corpusdict import compute_corpus_and_dict

corpus, dictionary = compute_corpus_and_dict()
#lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
#vec_lsi = lsi[vec_bow] # convert the query to LSI space
#print(vec_lsi)
