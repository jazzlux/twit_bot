#! /home/pi/Desktop/twitbot/tweet_env/bin/python

import tweepy
from dotenv import load_dotenv
import os
import csv

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
csv_path = "/home/pi/Desktop/twitbot/bot/movement_twits.csv"
#csv_path = "/home/pi/Desktop/twitbot/bot/test.csv"
#keywords_to_listen = "brexit"
keywords_to_listen = "movement director"

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")



# trends_result = api.trends_place(23424925)
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])

# Create a tweet
#api.update_status("Hello")


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
            try:
                t = status.extended_tweet['full_text']
            except AttributeError:
                #t='none'
                t = status.text
            twit = []
            twit.append(t)
            print(twit)
            with open(csv_path, mode='a', encoding='UTF-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(twit)


    def on_error(self, status):
        print("Error detected")
        print(status)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener, tweet_mode='extended')
stream.filter(track=[keywords_to_listen], languages=["en"])


# locations=[-9.0869,39.8009,-7.1542,40.5007]
"""File "/home/pi/Desktop/twitbot/tweet_env/lib/python3.5/site-packages/urllib3/response.py", line 430, in _error_catcher
    raise ReadTimeoutError(self._pool, None, "Read timed out.")
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='stream.twitter.com', port=443): Read timed out."""
