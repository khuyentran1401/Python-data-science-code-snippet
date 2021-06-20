# pip install textacy
# pip install spacy
# python -m spacy download en_core_web_sm

import pandas as pd 
import spacy 
from textacy.extract import ngrams

nlp = spacy.load('en_core_web_sm')

text = nlp('Data science is an inter-disciplinary field that uses'
' scientific methods, processes, algorithms, and systme to extract'
' knowledge and insights from many structural and unstructured data.')

n_grams = 2 # contiguous sequence of a word
min_freq = 1 # extract n -gram based on its frequency

print(pd.Series([n.text for n in ngrams(text, n=n_grams, min_freq=1)]).value_counts())
""" 
disciplinary field    1
scientific methods    1
unstructured data     1
Data science          1
extract knowledge     1
uses scientific       1
"""