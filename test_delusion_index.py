from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from corpusdict import compute_basics

concept_dict = get_concepts_from_files()
basics = compute_basics()
index_input(basics, concept_dict)
