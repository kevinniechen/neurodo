from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics, compute_basics_text
from get_num_determiners import get_num_determiners
from syntacticComplexity.maxPhraseLength import max_phrase_length_text
from semantic_coherence.semantic_coherence import index_string
from numpy import exp, cos, linspace
import os, time, glob, pickle

def unpack_data(textarea):
    return str(textarea.data)

def unpack_to_set(textarea):
    return set(unpack_data(textarea).splitlines())

def number_of_words(textset):
    return str(len(textset))

def calc_basics(text):
    return compute_basics_text(text, 'all')

def calc_delusions(text):
    default_delusion_categories = [
    'time',
    'self',
    'surveillance',
    'unfair',
    'mind_control',
    'alien',
    ]

    remove_delusions()
    add_delusions(default_delusion_categories)
    concept_dict = get_concepts_from_files()

    basics = calc_basics(text)
    smart_ave_dict = index_input(basics, concept_dict)
    return(smart_ave_dict)

def calc_coherence(text):
    return(index_string(text))

def calc_determiners(text):
    basics = calc_basics(text)
    word_count = 0
    for sentence in basics.words:
        for w in sentence:
            word_count += 1

    return get_num_determiners(text) / float(word_count)

def calc_phrase_len(text):
    return max_phrase_length_text(text) / 8.0

def calc_ml(coherence, determiners, phrase_len, a1, a2, a3, a4, a5, a6):
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

    x = [min(coherence), determiners, phrase_len, a1, a2, a3, a4, a5, a6]
    return loaded_model.predict(x)[0]
