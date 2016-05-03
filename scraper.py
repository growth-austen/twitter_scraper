import tweepy

#remember to add your cosumer/access keys and tokens

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print "Grabbing the tweets of %s" % consumer_key

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

results = api.search(q="@austenallred -RT")
for tweet in results:
	print "Tweet ID -> " + str(tweet.id)
	print "Tweet Text -> " + tweet.text 
	print "Tweet username -> " + tweet.author._json['screen_name']
	print "\n\n"