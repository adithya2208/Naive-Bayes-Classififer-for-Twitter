#!/usr/bin/python
import os,re,nltk
  

def remove_non_ascii(text):
    return "".join(filter(lambda x: ord(x)<128, text))  

def feature_extract(y):
    wnl = nltk.WordNetLemmatizer() 
    y=remove_non_ascii(y)
    y=nltk.word_tokenize(y)
    y=[j.lower() for j in y]
    for i in nltk.corpus.stopwords.words():
        while i in y:
            y.remove(i)
    y=[wnl.lemmatize(t) for t in y]
    y=[i.encode("utf-8") for i in y]
    while 'rt' in y:
        y.remove('rt')   
    x=list()
    for i in y:
        if re.search('^\w',i) == None:
            if i not in x:
                x.append(i) 
    for i in x:
        while i in y:
            y.remove(i)
    return y