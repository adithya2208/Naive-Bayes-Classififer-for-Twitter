#! /usr/bin/python
import tweepy,json,pickle,argparse,feature
parser=argparse.ArgumentParser()
parser.add_argument('keywords',help='list of keywords seperated by ,',type=str)
args=parser.parse_args()
keywords=args.keywords.split(',')
with open('keys.json','r') as f:
    auth_keys=json.load(f)

auth = tweepy.OAuthHandler(auth_keys['consumer_key'], auth_keys['consumer_secret'])
auth.set_access_token(auth_keys['access_token'], auth_keys['access_secret'])
api=tweepy.API(auth,wait_on_rate_limit=True)

file=open('classifier.pickle','rb')
cl=pickle.load(file)
file.close()

class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        tweepy.StreamListener.__init__(self)
        self.file1=open('tweets1','w')
        self.file2=open('tweets2','w')

    def on_status(self, status):
        print status.text
        text=status.text
        text=feature.feature_extract(text)
        clss=cl.classify(text)
        if clss=='1':
                self.file1.write(feature.remove_non_ascii(status.text)+'\n')
        else:
                self.file2.write(feature.remove_non_ascii(status.text)+'\n')
                

        


myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myStream.filter(track=keywords)