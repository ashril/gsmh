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

yesterday = date.today() - timedelta(1)
# yesterday = date.today()

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

# Create File Dataset
# Hapus dulu file yang lama
# os.remove("data_collections/dataset.csv")
csvFile = open("data_collections/dataset.csv",'a')
csvWriter = csv.writer(csvFile)
# tweets = tweepy.Cursor(api.search, q='ntb', lang="in", since=strftime("%Y-%m-%d", gmtime())).items(1000)
tweets = tweepy.Cursor(api.search, q='ntb', lang="in", since=yesterday.strftime('%Y-%m-%d')).items(1000)
for tweet in tweets:
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_dataset` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
    # Save to csv
    csvWriter.writerow([tweet.text])

tweets = tweepy.Cursor(api.search, q='ntb+lombok', lang="in", since=yesterday.strftime('%Y-%m-%d')).items(1000)
for tweet in tweets:
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_dataset` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
    # Save to csv
    csvWriter.writerow([tweet.text])

tweets = tweepy.Cursor(api.search, q='ntb+sumbawa', lang="in", since=yesterday.strftime('%Y-%m-%d')).items(1000)
for tweet in tweets:
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_dataset` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
    # Save to csv
    csvWriter.writerow([tweet.text])

tweets = tweepy.Cursor(api.search, q='ntb+bima', lang="in", since=yesterday.strftime('%Y-%m-%d')).items(1000)
for tweet in tweets:
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_dataset` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
    # Save to csv
    csvWriter.writerow([tweet.text])

tweets = tweepy.Cursor(api.search, q='ntb+dompu', lang="in", since=yesterday.strftime('%Y-%m-%d')).items(1000)
for tweet in tweets:
    hasil = sentiment(tweet.text)
    print("Tweets = ", tweet.text)
    print("Hasil Sentiment = ", hasil)
    sql_insert_query = """ INSERT INTO `get_dataset` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
    (NULL, %s, %s, %s, %s) """
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query, (str(tweet.created_at),str(tweet.user.screen_name),str(tweet.text),str(hasil)))
    connection.commit()
    # Save to csv
    csvWriter.writerow([tweet.text])

#Export to csv files
# export_query = """ SELECT * FROM get_dataset WHERE `tanggal` BETWEEN subdate(curdate(),1) AND curdate() INTO OUTFILE '/var/lib/mysql-files/today7.csv' fields terminated by '\t' enclosed by '"' escaped by '"' lines terminated by 'AUTO' """
# cursor = connection.cursor()
# result = cursor.execute(export_query)
# connection.commit()

print("Done........")
