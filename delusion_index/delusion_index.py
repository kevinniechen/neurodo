import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems

def index_input(basics, concept_dict):
    dictionary = basics.dictionary
    corpus = basics.corpus
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(basics.words))

    for name_of_concept, concept in concept_dict.items():
        print("==== " + name_of_concept)
        vec_bow = dictionary.doc2bow(concept)
        vec_lsi = lsi[vec_bow] # convert the query to LSI space
        index = similarities.MatrixSimilarity(lsi[corpus])
        sims = index[vec_lsi]
        #print_sorted_sims(sims, basics.words)
        small_lists = (sims[x:x+5] for x in range(0, len(sims), 5))
        maxes = [max(portion) for portion in small_lists]
        smart_ave = sum(maxes, 0.0) / len(maxes)

        print("==== " + name_of_concept + " = " + str(smart_ave))

def print_sorted_sims(sims, words):
    sims_sorted = sorted(enumerate(sims), key=lambda item: -item[1])
    for sim in sims_sorted:
        print(sim, words[sim[0]]) # print sorted (document number, similarity score) 2-tuples


