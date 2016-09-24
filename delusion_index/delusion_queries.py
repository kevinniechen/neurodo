import wget
import os

rel_query = "http://conceptnet5.media.mit.edu/data/5.4/search?rel=/r/RelatedTo&end=/c/en/"
assoc_query = "http://conceptnet5.media.mit.edu/data/5.4/assoc/list/en/"

def add_delusions(delusions):
    add_delusion_query(delusions, rel_query, 'rel', '&limit=20')
    add_delusion_query(delusions, assoc_query, 'assoc', '?limit=10')

def add_delusion_query(delusions, query, subdir, limit):
    for delusion in delusions:
        web_page = query + delusion + limit + "&filter=/c/en"
        out_file = os.path.join(os.getcwd(), "delusion_index", "delusions", subdir, delusion)
        if os.path.isfile(out_file):
            os.remove(out_file)
        print(web_page)
        file_name = wget.download(web_page, out=out_file)

def remove_delusions_subdir(subdir):
    dir = os.path.join(os.getcwd(), 'delusion_index', 'delusions', subdir)
    for file_name in os.listdir(dir):
        os.remove(os.path.join(dir, file_name))


def remove_delusions():
    remove_delusions_subdir('rel')
    remove_delusions_subdir('assoc')

