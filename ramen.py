"""
read_ramen.py
ラーメン店舗の追加や削除などを行うモジュール
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import re

def read_ramens(df):
    return df

def add_ramen(sentence):
    return None

def list_ramens(df):
    return df.name.tolist()

def set_ramen(sentences):
    with open("ramens_list.csv", "a") as f:
        f.write("{},{}\n".format(sentences[0], sentences[1]))
    print("Writed")

def head_tweets(url):
    # Access to URL
    soup = BeautifulSoup(urllib.request.urlopen(url))

    # head(3) tweets
    tweets = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[:3]

    for i, tweet in enumerate(tweets):
        if i == 0:
            text = "{:-<30}\n".format("")
        else:
            text += "{:-<30}\n".format("")
        text += re.sub("<.*?>","", str(tweet))
        text += "\n"

    return text
