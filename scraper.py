import tweepy
import csv

consumer_key = "###"
consumer_secret = "###"

access_token = "###"
access_token_secret = "###"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

outputFile = open('export.csv', 'a')
outputWriter = csv.writer(outputFile)

for tweet in tweepy.Cursor(api.search,
                       q="@austenallred -RT",
                       count=10000,
                       result_type="recent",
                       include_entities=True,
                       lang="en").items():
	print tweet.text
	outputWriter.writerow([tweet.text.encode('utf-8'),tweet.author._json['screen_name'],tweet.id])