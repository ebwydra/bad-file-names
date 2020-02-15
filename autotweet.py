import tweepy
from twitterauth import *
from filenamegenerator import *

### Authentication of consumer key and consumer secret ##
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

## Authentication of access token and access token secret ##
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Make a call to the badfilename() function ##
result = badfilename()
print(result)

## Send Tweet ##
while True:
    api.update_status(status = result)
    time.sleep(60*60) # once an hour
