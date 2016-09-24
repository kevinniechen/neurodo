import re
import itertools
import os

concept_dict = {}

def parse_file(file_name, file_path):
    concepts = []
    with open(file_path) as file:
        # find all quoted surfaceStart
        matches = re.findall(r'"start": "/c/en/(.+?)["/]', file.read().lower())
        concepts = list(itertools.chain.from_iterable(re.split('_', concept) for concept in matches))
        concepts.append(file_name)
        print(concepts)
    return concepts

def get_concepts_from_files():
    if not concept_dict:
        dir = os.path.join(os.getcwd(), 'delusion_index', 'delusions')
        for file_name in os.listdir(dir):
            concept_dict[file_name] = parse_file(file_name, os.path.join(dir, file_name))
    return concept_dict
