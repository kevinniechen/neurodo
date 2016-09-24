from corpusdict import compute_basics_text
from gensim import corpora, models, similarities
from scipy import spatial

def index_file(file_name):
    with open(file_name) as f:
        index_string(f.read())

def index_string(text):
    basics = index_coherence(compute_basics_text(text, 'all'), compute_basics_text(text, 'even'), compute_basics_text(text, 'odd'))

def make_model(corpus, dictionary, words):
    return models.LsiModel(corpus, id2word=dictionary, num_topics=len(words))

def index_coherence(basics, even_basics, odd_basics):
    lsi = make_model(basics.corpus, basics.dictionary,
            basics.words)
    sims = []
    for esentence, osentence in zip(even_basics.words, odd_basics.words):
        ovec_lsi = lsi[basics.dictionary.doc2bow(osentence)]
        evec_lsi = lsi[basics.dictionary.doc2bow(esentence)]

        if len(ovec_lsi) == len(evec_lsi):
            sims.append(1 - spatial.distance.cosine([e[1] for e in evec_lsi], [o[1] for o in ovec_lsi]))
        else:
            print(ovec_lsi[-1], evec_lsi[-1])
            print(len(ovec_lsi), len(evec_lsi))
    return sims


index_file('timecube_raw.txt')

index_string("""
In 1884,  meridian time personnel met
 in Washington to change Earth time.
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
""")
