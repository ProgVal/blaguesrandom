from time import *
import tweepy
from gen import *
from mastodon import Mastodon

passwords = open('keys.txt', 'r')

consumer_key = passwords.readline()[:-1]
consumer_secret = passwords.readline()[:-1]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_key = passwords.readline()[:-1]
access_secret = passwords.readline()[:-1]

auth.set_access_token(access_key, access_secret)

pass_mastodon = open('credentials.txt', 'r')

MASTODON_USERNAME = pass_mastodon.readline()[:-1]
MASTODON_PASSWORD = pass_mastodon.readline()[:-1]

MASTODON_BASE_URL = "https://mastodon.social"

mastodon_api = Mastodon(
    client_id = "mastodon_client.secret", 
    api_base_url = MASTODON_BASE_URL
)
mastodon_api.log_in(
    username = MASTODON_USERNAME, 
    password = MASTODON_PASSWORD, 
    to_file = "mastodon_user.secret",
    scopes = ["read", "write"]
)

api = tweepy.API(auth)

while True :
    g = blague(10)
    api.update_status(g)
    mastodon.status_post(g)
    print("Tweeting : ", g, " at ", asctime(localtime(time())))
    sleep(7200)
