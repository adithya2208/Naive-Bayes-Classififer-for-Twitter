#!/usr/bin/python
import os,random,nltk,feature,pickle
from argparse import ArgumentParser
from textblob.classifiers import NaiveBayesClassifier

def main():
    parser=ArgumentParser()
    parser.add_argument('train',help='size of train set',type=int)
    parser.add_argument('test',help='size of test set',type=int)
    args=parser.parse_args()
    os.chdir('Source')  
    feature_set=[]
    for k in ['1','2']:
        with open(k+'.txt','r') as f:
            temp=f.readlines()
        random.shuffle(temp)
        for i in range(args.train):
            feature_set.append((temp[i].rstrip(),k))
    random.shuffle(feature_set)
    print 'Training classifier'
    cl=NaiveBayesClassifier(feature_set[0:args.train])
    if args.test!=0:
        print 'The accuracy of the classifier with test data is ',cl.accuracy(feature_set[args.train:args.train+args.test])
        tp=tn=fp=fn=0.0
        for i in range(args.train,args.train+args.test):
            x=cl.classify(feature_set[i][0])
            if x=='1':
                if x==feature_set[i][1]:
                    tp+=1.0
                else:
                    fp+=1.0
            if x=='2':
                if x==feature_set[i][1]:
                    tn+=1.0
                else:
                    fn+=1.0
        print 'True Positive=',tp
        print 'True Negative=',tn
        print 'False Positive=',fp
        print 'False Negative=',fn
        p=tp/(tp+fp)
        r=tp/(tp+fn)
        f=2*p*r/(p+r)
        print "Precision=",p
        print "Recall=",r
        print "F measure=",f
    os.chdir('..')
    file=open('classifier.pickle','wb')
    pickle.dump(cl,file)
    file.close()



if __name__=="__main__":
    main()