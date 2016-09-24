import wget
import os

def add_delusions(delusions):
    for delusion in delusions:
        web_page = "http://conceptnet5.media.mit.edu/data/5.4/search?rel=/r/RelatedTo&end=/c/en/" + delusion + "&limit=20&filter=/c/en"
        print(web_page)
        out_file = os.path.join(os.getcwd(), "delusion_index", "delusions", delusion)
        if os.path.isfile(out_file):
            os.remove(out_file)
        file_name = wget.download(web_page, out=out_file)

def remove_delusions():
    dir = os.path.join(os.getcwd(), 'delusion_index', 'delusions')
    for file_name in os.listdir(dir):
        os.remove(os.path.join(dir, file_name))
