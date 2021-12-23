import nltk

from dictionary import Dictionary


class SentimentScore:
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

    tokenizer = nltk.tokenize.TweetTokenizer()
    tweet_words = tokenizer.tokenize(tweet)

    for word in tweet_words:
        negative_score += dictionaryN.check(word)

    for word in tweet_words:
        positive_score += dictionaryP.check(word)

    if negative_score > positive_score:
        return 'negative'
    elif negative_score == positive_score:
        return 'neutral'
    else:
        return 'positive'


def sentiment_analysis(tweets):
    negative_tweets = []
    positive_tweets = []

    for tweet in tweets:

        res = sentiment(tweet['text'])

        if res == 'negative':
            negative_tweets.append(tweet['text'])
        elif res == 'positive':
            positive_tweets.append(tweet['text'])

    return SentimentScore(positive_tweets, negative_tweets)
