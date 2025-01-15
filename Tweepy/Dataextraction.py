from flask import Flask, request, redirect
from pyngrok import ngrok
import tweepy

API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
CALLBACK_ROUTE = '/callback'

app = Flask(__name__)

@app.route('/')
def home():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, callback=REDIRECT_URI)
    try:
        # Redirect the user to Twitter for authorization
        redirect_url = auth.get_authorization_url()
        # Store the request token in a session or memory
        global request_token
        request_token = auth.request_token
        return redirect(redirect_url)
    except tweepy.TweepyException as e:
        return f"Error during authentication: {e}"

@app.route(CALLBACK_ROUTE, methods=['GET'])
def callback():
    # Handle the callback after the user authorizes the app
    verifier = request.args.get('oauth_verifier')
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY)

    # Use the request token to obtain an access token
    auth.request_token = request_token
    try:
        auth.get_access_token(verifier)
        access_token = auth.access_token
        access_token_secret = auth.access_token_secret

        # Store the access token and secret securely
        return f"Access Token: {access_token}, Access Token Secret: {access_token_secret}"
    except tweepy.TweepyException as e:
        return f"Error fetching access token: {e}"

ngrok.set_auth_token('2r2Ny4J06jKbuuUk8wKTG5ntup5_XFjmY9DLotPK5K87h2vS')

if __name__ == '__main__':
    port = 5000
    public_url = ngrok.connect(port)
    print(f' * ngrok tunnel "http://127.0.0.1:{port}" -> "{public_url.public_url}"')
    REDIRECT_URI = public_url.public_url + CALLBACK_ROUTE
    app.run(port=port)


from flask import Flask, request, redirect
from pyngrok import ngrok
import tweepy

# Replace with your actual Twitter API credentials
API_KEY = 'OANv6aaYdK0qsNuhcqPuLWZT5'
API_SECRET_KEY = ''
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
CALLBACK_ROUTE = '/callback'

app = Flask(__name__)

# Store the request token globally
request_token = None

@app.route('/')
def home():
    # Step 1: Initiate the OAuth process
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, callback=REDIRECT_URI)
    try:
        # Step 2: Get the authorization URL and redirect user to Twitter
        redirect_url = auth.get_authorization_url()
        global request_token
        request_token = auth.request_token
        return redirect(redirect_url)
    except tweepy.TweepyException as e:
        return f"Error during authentication: {e}"

@app.route(CALLBACK_ROUTE, methods=['GET'])
def callback():
    # Step 3: Handle the callback after user authorization
    verifier = request.args.get('oauth_verifier')
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY)

    # Step 4: Obtain the access token using the verifier
    auth.request_token = request_token
    try:
        auth.get_access_token(verifier)
        access_token = auth.access_token
        access_token_secret = auth.access_token_secret

        # Step 5: Store the access token and secret securely
        return f"Access Token: {access_token}, Access Token Secret: {access_token_secret}"

    except tweepy.TweepyException as e:
        return f"Error fetching access token: {e}"

# Function to fetch tweets with a specific hashtag
def fetch_tweets(hashtag, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        # Fetch tweets with the given hashtag
        tweets = api.search_tweets(q=hashtag, count=10, lang="en")
        for tweet in tweets:
            print(f"{tweet.user.screen_name}: {tweet.text}")
    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")

# Function to post a tweet
def post_tweet(content, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        # Post a tweet with the provided content
        api.update_status(status=content)
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# ngrok setup
ngrok.set_auth_token('2r2Ny4J06jKbuuUk8wKTG5ntup5_XFjmY9DLotPK5K87h2vS')

if __name__ == '__main__':
    port = 5000
    public_url = ngrok.connect(port)
    print(f' * ngrok tunnel "http://127.0.0.1:{port}" -> "{public_url.public_url}"')
    REDIRECT_URI = public_url.public_url + CALLBACK_ROUTE
    app.run(port=port)

    # Example usage after successful authentication (replace with actual access token)
    # Once you have the access token from the callback, you can fetch and post tweets like this:
    # access_token = 'your_access_token'
    # access_token_secret = 'your_access_token_secret'
    # fetch_tweets("#icc", access_token, access_token_secret)
    # post_tweet("Loving the ICC cricket updates! #icc", access_token, access_token_secret)
import tweepy

# Replace with your actual Twitter API credentials
API_KEY = ''
API_SECRET_KEY = ''  # Replace with your API Secret Key
ACCESS_TOKEN = ''  # Replace with your Access Token
ACCESS_TOKEN_SECRET = ''  # Replace with your Access Token Secret

# Authenticate with Twitter using the access token and secret
auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

# Fetch tweets with #hashtag
def fetch_tweets(hashtag):
    try:
        tweets = api.search_tweets(q=hashtag, count=10, lang="en")  # Fetch 10 tweets with the hashtag
        for tweet in tweets:
            print(f"{tweet.user.screen_name}: {tweet.text}")
    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")

# Fetch tweets with #icc
print("Fetching tweets with #icc:")
fetch_tweets("#icc")
