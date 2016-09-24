from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics, compute_basics_text
from numpy import exp, cos, linspace
import os, time, glob

def unpack_data(textarea):
    return str(textarea.data)

def unpack_to_set(textarea):
    return set(unpack_data(textarea).splitlines())

def number_of_words(textset):
    return str(len(textset))

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

    basics = compute_basics_text(text, 'all')
    smart_ave_dict = index_input(basics, concept_dict)
    return(smart_ave_dict)
