#!/usr/bin/python
import sys,os,random,feature,nltk

os.chdir('Source')
document=[]
for i in ['1','2']:
    os.chdir(i)
    list=[x for x in os.listdir('.') if x.endswith('.txt')]
    for j in list:
        with open(j,'r') as f:
            x=f.readlines()
            for t in x:
                document.append((t.rstrip(),i))
    os.chdir('..')

with open('1.txt','w') as f1:
    with open('2.txt','w') as f2:
        for i in document:
            if i[1]=='1':
                f1.write(i[0]+'\n')
            else:
                f2.write(i[0]+'\n')
