import tweepy
from dotenv import load_dotenv
import os
import csv

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


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
            t = status.text
            print(t)
            # twit = []
            # twit.append(t)
            # with open('twit.csv', mode='a') as csvfile:
            #     writer = csv.writer(csvfile)
            #     writer.writerow(twit)


    def on_error(self, status):
        print("Error detected")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)



tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["@GretaThunberg"], languages=["en"])


# locations=[-9.0869,39.8009,-7.1542,40.5007]
