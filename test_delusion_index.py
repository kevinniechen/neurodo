from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics

remove_delusions()
add_delusions([
'time',
'sense',
'attempt',
'get',
'distress',
'self',
    ])
concept_dict = get_concepts_from_files()
basics = compute_basics()
index_input(basics, concept_dict)
