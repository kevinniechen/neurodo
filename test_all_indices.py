from semantic_coherence import semantic_coherence
import glob
from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics, compute_basics_text
from get_num_determiners import get_num_determiners
from syntacticComplexity.maxPhraseLength import maxPhraseLength

default_delusion_categories = [
'time',
'self',
'surveillance',
'unfair',
'mind_control',
'alien',
]

def delusion_index_file(file_name, concept_dict):
    basics = compute_basics(file_name)
    return index_input(basics, concept_dict), basics

def delusion_index_string(text, concept_dict):
    basics = compute_basics_text(text, 'all')
    return index_input(basics, concept_dict)

def get_det_file(file_name):
    with open(file_name) as f:
        return get_num_determiners(f.read())
    return 0

def test_dir(dir_name, concept_dict, results_dict):
    for file_name in glob.glob(dir_name + '/*.txt'):
        print(file_name)
        sims = semantic_coherence.index_file(file_name)
        delu, basics = delusion_index_file(file_name, concept_dict)
        num_det = get_det_file(file_name) / float(len(basics.words))
        max_phrase_len = maxPhraseLength(file_name)
        pprint(delu)


        results_dict[file_name] = [
                min(sims),
                num_det,
                max_phrase_len,
                delu[default_delusion_categories[0]],
                delu[default_delusion_categories[1]],
                delu[default_delusion_categories[2]],
                delu[default_delusion_categories[3]],
                delu[default_delusion_categories[4]],
                delu[default_delusion_categories[5]]
        ]
        #print(sum(delu.values()))
        #print("sims min: " + str(min(sims)))
        #print("delu max: " + str(max(delu.values())))
        #print("num_det: " + str(num_det))
        #print("max_phrase_len: " + str(max_phrase_len))
        #results_dict[file_name] = [min(sims),
    return results_dict

def run_all_tests():
    remove_delusions()
    add_delusions(default_delusion_categories)
    concept_dict = get_concepts_from_files()

    results_dict = {}
    test_dir('control_data', concept_dict, results_dict)
    test_dir('patient_data', concept_dict, results_dict)
    return results_dict

run_all_tests()
