import re

import mysql.connector
import nltk.classify.util
import tweepy
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from api import api
from api import twitter
from dictionary import Dictionary
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from twython import Twython
import bcrypt


# def mysql_get_mydb():
#     try:
connection = mysql.connector.connect(host='localhost', database='prcc_ntb', user='root', password='huruhara')
# except mysql.connector.Error as err:
#     if err.errno == mysql.connector.errors.ERR_ACCESS_DENIED_ERROR:
#         print("Ada Masalah Dengan Username & Password Anda")
#     elif err.errno == mysql.connector.errors.ERR_BAD_DV_ERROR:
#         print("Database tidak tersedia")
#     else:
#         print(err)
# else:
#     connection.close()
#
# return connection

factory = StemmerFactory()
stemmer = factory.create_stemmer()

app = Flask(__name__)
app.secret_key = '01234567890~!@#$%^&*()_+prccntb!'

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

# New Update Login
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # cur = mysql.connection.cursor()
        cursor = connection.cursor()
        # cur.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username, hash_password,))
        cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username, hash_password,))
        # mysql.connection.commit()
        connection.commit()
        session['username'] = request.form['username']
        return redirect(url_for('home'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        cursor = connection.cursor(dictionary=True)
        # curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        # curl.execute("SELECT * FROM users WHERE username=%s", (username,))
        # user = curl.fetchone()
        user = cursor.fetchone()
        cursor.close()

        if len(user) > 0:
            print(user)
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['username'] = user['username']
                return redirect(url_for('home'))
            else:
                return "Error username and password"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")


@app.route('/home')
def home():
    # mysql_get_mydb()
    cursor = connection.cursor()
    query = "SELECT * FROM pop_keywords WHERE pop_keywords.tanggal = CURDATE()"
    #query = "SELECT * FROM pop_keywords WHERE tanggal LIKE '2019-11-29' ORDER BY  `pop_keywords`.`id` ASC "
    #query = "SELECT * FROM pop_keywords WHERE tanggal LIKE '2019-03-19' AND kab_kota='B3M3'"
    cursor.execute(query)
    rows1 = cursor.fetchall()
    connection.commit()

    # Facebook
    query = "SELECT * FROM kota_mataram  limit 0,5"
    # cursor = connection.cursor()
    cursor.execute(query)
    rows2 = cursor.fetchall()
    # connection.commit()    
    

    # query = "SELECT * FROM kota_mataram  limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows2 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_loteng limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows3 = cursor.fetchall()
    # # connection.commit()

    # query = "SELECT * FROM kota_mataram  limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows2 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_loteng limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows3 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_lobar limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows4 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_lombokutara limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows5 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_lotim limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows6 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_sumbawa limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows7 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_sumbawabarat limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows8 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_bima limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows9 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kota_bima limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows10 = cursor.fetchall()
    # # connection.commit()
    #
    # query = "SELECT * FROM kab_dompu limit 0,5"
    # # cursor = connection.cursor()
    # cursor.execute(query)
    # rows11 = cursor.fetchall()
    # connection.commit()

    p = []
    p.append(rows1)
    p.append(rows2)
    # p.append(rows3)
    # p.append(rows4)
    # p.append(rows5)
    # p.append(rows6)
    # p.append(rows7)
    # p.append(rows8)
    # p.append(rows9)
    # p.append(rows10)
    # p.append(rows11)
    # connection.close()
    return render_template('home.html', result=p)


@app.route('/layanan')
def layanan():
    return render_template('layanan.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":

        query_search = twitter.cursor(twitter.search, q=request.form['inputKeyword'])
        # query_search = tweepy.Cursor(api.search, q=request.form['inputKeyword'])

        return render_template("result.html", result=sentiment_analysis(query_search),
                               keyword=request.form['inputKeyword'])
    else:
        return render_template("layanan.html")


@app.route('/daily')
def daily():
    query = "SELECT * FROM get_dataset where status='positive' ORDER BY id DESC LIMIT 0,50"
    # query = "SELECT * FROM daily WHERE (tanggal = CURRENT_DATE) AND (status = 'positive') limit 0,10"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()

    query = "SELECT * FROM get_dataset where status='negative' ORDER BY id DESC LIMIT 0,50"
    # query = "SELECT * FROM daily WHERE (tanggal = CURRENT_DATE) AND (status = 'negative') limit 0,10"
    cursor = connection.cursor()
    cursor.execute(query)
    rows2 = cursor.fetchall()
    connection.commit()

    p = []
    p.append(rows)
    p.append(rows2)

    return render_template("daily2.html", result=p)


# @app.route('/get_daily', methods=['POST'])
# def get_daily():
#     tweets = tweepy.Cursor(api.search, q='ntb', lang="in", since='2019-02-19').items(5000)

#     for tweet in tweets:
#         hasil = sentiment(tweet.text)
#         print("Tanggal = ", tweet.created_at)
#         print("User = ", tweet.user.screen_name)
#         print("Tweets = ", tweet.text)
#         print("Hasil Sentiment = ", hasil)
#         print()
#         sql_insert_query = """ INSERT INTO `daily` (`id`, `tanggal`, `user`, `text`, `status`) VALUES 
#         (NULL, %s, %s, %s, %s) """
#         cursor = connection.cursor()
#         result = cursor.execute(sql_insert_query,
#                                 (str(tweet.created_at), str(tweet.user.screen_name), str(tweet.text), str(hasil)))
#         connection.commit()
#     print("Done........")
#     return render_template("daily2.html", result=result)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pengujian')
def wsentiment():
    return render_template('daily.html')


@app.route('/kb')
def kata_baku():
    query = "SELECT * FROM kelas_kata limit 10"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    return render_template('kata_baku.html', kelas_kata=rows)


@app.route('/ktb')
def kata_tidak_baku():
    query = "SELECT * FROM alias limit 10"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    return render_template('kata_baku.html', kelas_kata=rows)


@app.route('/dt')
def data_training():
    query = "SELECT * FROM kelas_kata limit 10"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    return render_template('kata_baku.html', kelas_kata=rows)


@app.route('/trending')
def trending():
    return render_template('trending.html')


if __name__ == '__main__':
    # app.run(debug=True, host='36.91.156.2', port='5000')
    app.run(debug=True, host='localhost', port='5000')
