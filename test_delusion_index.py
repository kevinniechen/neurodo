from pprint import pprint  # pretty-printer
from delusion_index.delusion_index import index_input
from delusion_index.conceptnet5parser import get_concepts_from_files
from delusion_index.delusion_queries import add_delusions, remove_delusions
from corpusdict import compute_basics, compute_basics_text

default_delusion_categories = [
'time',
'self',
'surveillance',
'unfair',
'mind_control',
'alien',
]

def index_file(file_name, concept_dict):
    basics = compute_basics(file_name)
    smart_ave_dict = index_input(basics, concept_dict)
    print(file_name)
    pprint(smart_ave_dict)

def index_string(text, concept_dict):
    basics = compute_basics_text(text, 'all')
    smart_ave_dict = index_input(basics, concept_dict)
    pprint(smart_ave_dict)


remove_delusions()
add_delusions(default_delusion_categories)
concept_dict = get_concepts_from_files()
#index_file('timecube_raw.txt', concept_dict)
#index_file('control_raw.txt', concept_dict)


for x in range(0, 6):
    index_file('ctl_pres_' + str(x) + '_raw.txt', concept_dict)
for x in range(0, 2):
    index_file('schiz_' + str(x) + '_raw.txt', concept_dict)



index_string("""
In 1884,  meridian time personnel met
 in Washington to change Earth time.
First words said was that only 1 day
could be used on Earth to not change
 the 1 day bible. So they applied the 1
day  and  ignored  the  other  3 days.
The bible time was wrong then and it
 proved wrong today. This a major lie
  has so much evil feed from it's wrong.
No man on Earth has no belly-button,
  it proves every believer on Earth a liar.
""", concept_dict)
