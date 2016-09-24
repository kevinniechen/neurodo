import re
import itertools
import os
from collections import defaultdict
from pprint import pprint  # pretty-printer

concept_dict = defaultdict(list)

def parse_file(file_name, file_path, subdir):
    concepts = []
    if subdir == 'assoc' and file_name == 'time':
        return concepts
    search_string = r''
    if subdir == 'rel':
        search_string = r'"start": "/c/en/(.+?)["/]'
    else:
        search_string= r'"/c/en/(.+?)["/]'
    with open(file_path) as file:
        # find the words returned from the query in the json file
        matches = re.findall(search_string, file.read().lower())
        concepts = list(itertools.chain.from_iterable(re.split('_', concept) for concept in matches))
        # add the parent concept itself
        concepts.append(file_name)
        # here we'll get rid of some undesirable related words which
        # don't imply delusions/obsessions
        if "always" in concepts:
            concepts.remove("always")
        print(concepts)
    return concepts

def get_concepts_from_subdir(subdir):
        dir = os.path.join(os.getcwd(), 'delusion_index', 'delusions', subdir)
        for file_name in os.listdir(dir):
            concept_dict[file_name] += parse_file(file_name, os.path.join(dir, file_name), subdir)

def get_concepts_from_files():
    if not concept_dict:
        print("got here")
        get_concepts_from_subdir('rel')
        get_concepts_from_subdir('assoc')
        pprint(concept_dict)
    return concept_dict
