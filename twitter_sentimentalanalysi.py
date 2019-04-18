import tweepy
from textblob import TextBlob

consumer_key = "eVzpDSlfBp29JWMPKzDgp0x4b"
consumer_secret = "5lGpNQIcni5VhMhZyfsZIVUkvrF5aqYXFslahRHBeBZlqNM1Cf"

access_token = "2837991853-A0rnt8Il8qZPnBxxGWLLe5QBAlmPaeEDaHuEsFc"
access_token_secret = "KRsBwc6Ob9wCpKh95nQycZCgYP6egoooOqwEKuch9Qr2l"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Kamalhassan")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)