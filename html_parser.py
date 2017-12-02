#!/usr/bin/python
import nltk,bs4,os,sys,feature
os.chdir('Source')
for i in ('1','2'): 
    os.chdir(i)
    y=list()
    dir_list=[x for x in os.listdir('.') if x.endswith(".html")]
    for k in dir_list:
        print k
        with open(k,'r') as f:
            soup=bs4.BeautifulSoup(f.read(),'html.parser')
            for j in soup.find_all('script')+soup.find_all('img')+soup.find_all('noscript')+soup.find_all('style'):
                j.decompose()
            y=soup.get_text()
            y=feature.feature_extract(y)
            y="\n".join(y)
        k=k+'.txt'
        with open(k,'w') as f:
            f.write(y)
    os.chdir('..')
    
    
    
    
    
    
