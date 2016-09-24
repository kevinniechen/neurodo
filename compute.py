from numpy import exp, cos, linspace
import os, time, glob

def unpack_data(textarea):
    return textarea.data

def unpack_to_set(textarea):
    return set(unpack_data(textarea).splitlines())

def number_of_words(textset):
    return str(len(textset))
