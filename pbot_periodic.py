import tweepy
from dotenv import load_dotenv
import os
import csv
import json
from ftplib import FTP

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# csv_path = "/Users/Pete/Desktop/Pi/tweetbot/bot/twit.csv"
keyword = "remote job"
json_filename = "jsonList_test.json"


def search_for_tweets(keyword):

    lista = []

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)


    for tweet in api.search(q=keyword, lang="en", count=20, include_entities=True):
        # for tweet in api.search(q=keyword, lang="en", count=20, include_entities=True):
        dict = {}

        for url in tweet.entities['urls']:

             url = url['expanded_url']
             cont = tweet.text
             dict.update(url=url, content = cont)

        if len(dict) == 0:
            print("empty")
        else:
            lista.append(dict)
        # lista.append(dict)

    return lista

# search_for_tweets(keyword)



def save_to_json(filename):
    with open(filename, mode='w') as file:
        results = search_for_tweets(keyword)
        json.dump(results, file)
        print(results)
    try :
        dump_to_ftp()
    except:
        print("some error on line")


def dump_to_ftp():
    server = os.getenv('FTP_SERVER')
    user = os.getenv('FTP_USER')
    password = os.getenv('FTP_PASS')
    # print(server, user, password)

    file = open(json_filename, mode="rb")
    # loaded_json = json.load(jfile)
    # print(loaded_json)

    ftp = FTP(server)
    #ftp.set_debuglevel(1)
    ftp.connect(server, 21)
    ftp.login(user, password)
    print(ftp.getwelcome())

    ftp.cwd('domains/zielewski.com/private_html')
    ftp.storbinary("STOR " + json_filename, file)   # send the file
    ftp.quit()

save_to_json(json_filename)
# dump_to_ftp()
