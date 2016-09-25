from corpusdict import compute_basics_text
from gensim import corpora, models, similarities
from scipy import spatial

def index_file(file_name):
    sims = []
    with open(file_name) as f:
        sims = index_string(f.read())
    return sims

def index_string(text):
    return index_coherence(compute_basics_text(text, 'all'), compute_basics_text(text, 'even'), compute_basics_text(text, 'odd'))

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
        #else:
        #    print(ovec_lsi[-1], evec_lsi[-1])
        #    print(len(ovec_lsi), len(evec_lsi))

    if not sims:
        sims = [0]
    return sims
