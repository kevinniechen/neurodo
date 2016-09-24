import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems

def index_input(basics, concept_dict):
    dictionary = basics.dictionary
    corpus = basics.corpus
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(basics.words))
    doc = "time"


    vec_bow = dictionary.doc2bow(concept_dict["time"])
    #vec_bow = dictionary.doc2bow("time".lower().split())

    vec_lsi = lsi[vec_bow] # convert the query to LSI space
    index = similarities.MatrixSimilarity(lsi[corpus])
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    for sim in sims:
        print(sim, basics.words[sim[0]]) # print sorted (document number, similarity score) 2-tuples
