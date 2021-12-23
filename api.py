import tweepy
# from twython import Twython

# # KEY ASHRIL
# APP_KEY = 'Z2gdnGoZPlYubERqas5zTVAFO'
# APP_SECRET = '8H5EntuYeq4gkxdhaZVZk2pmERcoqTlNr0Enys7fw1a1DoXOT2'


# twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
# ACCESS_TOKEN = twitter.obtain_access_token()

# twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# ACCESS TOKEN ASHRIL
consumer_key = 'Z2gdnGoZPlYubERqas5zTVAFO'
consumer_secret = '8H5EntuYeq4gkxdhaZVZk2pmERcoqTlNr0Enys7fw1a1DoXOT2'
access_token = '297272903-eLDCXtTCFK4rKlp6uk1w8yIvHkJ4Wvpk3KteRck9'
access_token_secret = 'f97dxy7Ok9JekRyP4k7um7ZnxS8TwfNsS2Az4yE5ETClg'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



# import tweepy
# from twython import Twython

# APP_KEY = 'Pf0GWhAmIyh9jpA0tqjqHbOCB'
# APP_SECRET = 'NhShXPAvraIEzD79iLWGqQGWZMwQZjr83mgvF8H2CbnhdeYey0'

# twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
# ACCESS_TOKEN = twitter.obtain_access_token()

# twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


# consumer_key = 'Pf0GWhAmIyh9jpA0tqjqHbOCB'
# consumer_secret = 'NhShXPAvraIEzD79iLWGqQGWZMwQZjr83mgvF8H2CbnhdeYey0'
# access_token = '1029826110-bGYr6Rvfok7r9bMSA0arzuWoKV1b3nOqWQpDgxR'
# access_token_secret = '4BZQHqZPWmelcv9j70IMG91SicxVxZiN2FxrwAaauSuko'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)
