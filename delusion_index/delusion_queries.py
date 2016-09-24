import wget
import os

delusion = 'time'
web_page = "http://conceptnet5.media.mit.edu/data/5.4/search?rel=/r/RelatedTo&end=/c/en/" + delusion + "&limit=20&filter=/c/en"

out_file = os.path.join(os.getcwd(), "delusion_index", "delusions", delusion)
if os.path.isfile(out_file):
    os.remove(out_file)
file_name = wget.download("http://conceptnet5.media.mit.edu/data/5.4/search?rel=/r/RelatedTo&end=/c/en/time&limit=20&filter=/c/en", out=out_file)

#-O "delusions/time"
