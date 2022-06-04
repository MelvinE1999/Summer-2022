from time import strftime
import stuff # holds my info
import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= stuff.keys.get('con_key')
consumer_secret= stuff.keys.get('con_sec')

access_token= stuff.keys.get('api_tok')
access_token_secret= stuff.keys.get('tok_key')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
