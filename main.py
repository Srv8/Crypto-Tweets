import os
import tweepy
import requests
import datetime

# Twitter API Details
api_key = os.environ['API_KEY']
api_secret = os.environ['API_KEY_SECRET']
bearer_token = os.environ['BEARER_TOKEN']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# To Auth
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to retrieve top 5 cryptocurrency data
def get_top_5_crypto_data():
    url = "https://api.coinlore.net/api/tickers/"
    response = requests.get(url)
    data = response.json()
    top_5_crypto_data = data['data'][:5]
    return top_5_crypto_data

# Function to create and post separate tweets for the top 5 cryptocurrencies
def post_top_5_crypto_tweets():
    top_5_crypto_data = get_top_5_crypto_data()
    
    for crypto in top_5_crypto_data:
        tweet = f"🚀 {crypto['name']} ({crypto['symbol']}) Stats 🚀\n\n"
        tweet += f"Price (USD): ${crypto['price_usd']}\n"
        tweet += f"24h % Change: {crypto['percent_change_24h']}%\n"
        tweet += f"24h Trading Volume: ${crypto['volume24']}\n"
        tweet += f"Market Cap (USD): ${crypto['market_cap_usd']}\n\n"
        tweet += f"📅 Date: {datetime.date.today()}\n"
        tweet += f"ℹ️ Good information here...\n\n"
        tweet += f"#Crypto #{crypto['symbol']} #YourHashtags"  # Using the cryptocurrency symbol as a hashtag

        # Create and post the tweet for each cryptocurrency
        client.create_tweet(text=tweet)

# Post separate tweets for the top 5 cryptocurrencies
post_top_5_crypto_tweets()
