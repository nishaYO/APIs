import tweepy

# Set your API keys and access tokens
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
api_key = 'your_api_key'
api_key_secret = 'your_api_key_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Specify the username for which you want to get the ID
username = 'elonmusk'

# Get user details
user = api.get_user(screen_name=username)
user_id = user.id_str
# Print user ID
print(f'Twitter ID for {username}: {user_id}')
