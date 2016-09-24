import logging
from collections import defaultdict
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from six import iteritems

def index_input(basics, concept_dict):
    dictionary = basics.dictionary
    corpus = basics.corpus
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(basics.words))
    smart_ave_dict = {}
    for name_of_concept, concept in concept_dict.items():
        vec_bow = dictionary.doc2bow(concept)
        vec_lsi = lsi[vec_bow] # convert the query to LSI space
        index = similarities.MatrixSimilarity(lsi[corpus])
        sims = index[vec_lsi]

        #print("==== " + name_of_concept)
        #print_sorted_sims(sims, basics.words)
        #print("==== " + name_of_concept)

        #small_lists = (sims[x:x+5] for x in range(0, len(sims), 5))
        #maxes = [max(portion) for portion in small_lists]
        #smart_ave_dict[name_of_concept] = sum(maxes, 0.0) / len(maxes)
        smart_ave_dict[name_of_concept] = sum(sims, 0.0) / len(sims)

    return smart_ave_dict

def print_sorted_sims(sims, words):
    sims_sorted = sorted(enumerate(sims), key=lambda item: -item[1])
    for sim in sims_sorted:
        print(sim, words[sim[0]]) # print sorted (document number, similarity score) 2-tuples


