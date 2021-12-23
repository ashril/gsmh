import re
import datetime
from time import gmtime, strftime
from datetime import date, timedelta

import csv
import json
import os
from urllib.parse import urlparse

import mysql.connector
import nltk.classify.util
import tweepy
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from flask import Flask
from flask import render_template, request

from api import api
from api import twitter
from dictionary import Dictionary

connection = mysql.connector.connect(host='localhost', database='prcc_ntb', user='root', password='huruhara', charset= 'utf8mb4')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

class SentimentScore(object):
    def __init__(self, positive_tweets, negative_tweets):
        self.positive_tweets = positive_tweets
        self.negative_tweets = negative_tweets
        self.neg = len(negative_tweets)
        self.pos = len(positive_tweets)


dictionaryN = Dictionary('negative-words.txt')
dictionaryP = Dictionary('positive-words.txt')


def sentiment(tweet):
    negative_score = 0
    positive_score = 0

    stemmer_tweets = stemmer.stem(tweet)
    tokenizer = nltk.tokenize.TweetTokenizer()
    tweet_words = tokenizer.tokenize(stemmer_tweets)

    for word in tweet_words:
        negative_score += dictionaryN.check(word)

    for word in tweet_words:
        positive_score += dictionaryP.check(word)

    if negative_score > positive_score:
        return 'negative'
    else:
        return 'positive'


def sentiment_analysis(tweets):
    negative_tweets = []
    positive_tweets = []

    for tweet in tweets:

        res = sentiment(tweet['text'])

        if res == 'negative':
            negative_tweets.append(tweet['text'])
        else:
            positive_tweets.append(tweet['text'])

    return SentimentScore(positive_tweets, negative_tweets)

tweets = tweepy.Cursor(api.search, q='bang zul', count=1000, lang="in", since="2020-01-01").items(10000)
for tweet in tweets:
    # csvWriter.writerow([tweet.text])
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_tokoh` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
 

print("Done........")
