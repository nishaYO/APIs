import tweepy

# Set your API keys and access tokens
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
api_key = 'your_api_key'
api_key_secret = 'your_api_key_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Post a tweet
tweet_text = "This tweet is done using twitter API."
api.update_status(status=tweet_text)
print("Tweet posted successfully!")