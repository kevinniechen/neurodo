import re
import itertools
import os

concept_dict = {}

def parse_file(file_name):
    concepts = []
    with open(file_name) as file:
        # find all quoted
        matches=re.findall(r'\"/c/en/(.+?)\"', file.read().lower())
        concepts = list(itertools.chain.from_iterable(re.split('_', concept) for concept in matches))
        print(concepts)
    return concepts

def get_concepts_from_files():
    if not concept_dict:
        dir = os.path.join(os.getcwd(), 'delusion_index', 'delusions')
        for file_name in os.listdir(dir):
            concept_dict[file_name] = parse_file(os.path.join(dir, file_name))
    return concept_dict
