#Neurodo

A python-based web-app that predicts the onset of schizophrenia and the current severity of positive symptoms (such as delusions) and negative symptoms (such as cognitive dysfunction) based on linguistic features in patient text samples. This project was a Top 10 Finalist and won Wolfram's Best Tech award at Johns Hopkins' MedHacks. [Devpost](https://devpost.com/software/cohere-013ltc).

#Installation

Here's how to run a local copy of Neurodo.

Instructions for Ubuntu or Debian, but should be easily adaptable to other Linux distributions or OS X. You will need Python 3.4 or newer. Depending on your set up, you might need to run the interpreter with `python` or `python3`. 

We suggest setting up a a Python [virtualenv](http://virtualenv.readthedocs.io/en/latest/userguide/#usage) for this project, or using another similar service.

```bash
# Clone repository
git clone https://github.com/stevengriffin/cohere_proj
cd cohere_proj

# Install needed system packages
sudo apt-get install python3 python-pip python3.4-dev gfortran libopenblas-dev liblapack-dev

# Install needed python packages
python3 -m pip install scipy numpy gensim wtforms Flask uwsgi nltk

# Run tests
python3 test_all_indices.py > log.txt

# Run a local copy of the website
python3 controller.py
# To see the website, navigate to http://0.0.0.0:5000/ in a web browser
# To stop running the local copy, press CTRL-C in the terminal you used to start it
```

#Background

Existing mental health apps often ask patients to rate the severity of their current issues or to self-apply cognitive behavioral techniques. However, patients with schizophrenia usually have difficulties with insight.

Natural language processing techniques have been used in the past to diagnose schizophrenia or predict the onset of psychosis in at-risk populations. In these papers, conversations with a practitioner are manually transcribed and serve as a single data point to predict current and future mental health.

These techniques work because thought-disordered speech has many common characteristics such as a unique approach to linkage (for example, connecting ideas based on their sounds or rhyming rather than topic as in clanging or omitting linkages like "That reminds me of ...").

With the advent of widespread computer and smartphone use even among low-income populations, we now have access to immediately analyzable textual data. Endeavors that used to require hundreds of hours of manual transcription, parsing, and analysis can be accomplished in an instant with modern NLP techniques and hardware.

#Function

Our webapp allows patients with thought disorders such as schizophrenia and schizoaffective disorder to track improvements to cognitive dysfunction and delusions over time, so that they can assess the efficacy of different medications and therapy techniques.

A patient can journal directly on the website or transfer their writings from another source such as a Word document or blog. Our backend analyzes the text by applying LSA to study semantic coherence and delusional content and traditional NLP parsing to study syntactic complexity. Machine learning unites these models to evaluate the author's progress with a graph.

#Stack

NLTK to parse and analyze linguistic syntax.

gensim LSA for efficient, scalable latent semantic analysis of text.

ConceptNet5 for word relations and associations concerning common delusions and fixations in psychosis.

SCIKIT for machine learning to build a robust predictive model from our combined semantic and syntactic analyses.

Flask and Materialize for rapid web development.

To speedily serve all of this complex analysis to our users we use Amazon EC2 hosting.

#What's next

Visual design and UI refinement, advertising, building a community. Making it fun to use by rewarding progress and encouraging perseverance.

Letting the user add custom delusionary thought themes that they are working on treating with their mental health practitioners.

Allowing the user to pull text automatically from supplied accounts on a list of supported websites and apps.

More data and more learning!

#Authors

Kevin Chen, kev@umd.edu

Steven Griffin, stevengriffin323@gmail.com

William Shyr

Daniel Hsu

Jeff Lai
