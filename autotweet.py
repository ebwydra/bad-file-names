import tweepy
# from twitterauth import *
from os import environ
from filenamegenerator import *

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


### Authentication of consumer key and consumer secret ##
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

## Authentication of access token and access token secret ##
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    ## Make a call to the badfilename() function ##
    result = badfilename()
    ## Send Tweet ##
    api.update_status(status = result)
    time.sleep(60) # once a minute
