# Naive-Bayes-Classififer-for-Twitter

## What is a Navie Bayes Classifier?
Naive Bayes classifier is a probablistic classification model that can group variables in the most porbably category out of two given categories. This classifier classifies the tweets from Twitter's public stream in either category 1 or category 2.

## Installation

This package requires nltk,textblob and tweepy python modules.
1) git clone https://github.com/adithya2208/Naive-Bayes-Classififer-for-Twitter.git
2) cd cd Naive-Bayes-Classififer-for-Twitter/
3) make
4) ** Copy html files related to your category into Sources/1 and Sources/2 directories which correspond to category 1 or category 2. For example, if you wish to determine if the tweet 'Apple is good for your health' refers to Apple Inc or the fruit. You need a html files related to Apple computers and the fruit in the two directories. Lexical information will be extracted from these html files. The quality of the classififer depends on the quality of the supplied html pages.**
5) make install TRAIN=*number of train datasets(words for training)* TEST=*number of test datasets(words for testting the classifier)*
6)./nbs.py *keywords(delimited by ,)*. Keywords refer to the keywords to scan the twitter public stream for.
