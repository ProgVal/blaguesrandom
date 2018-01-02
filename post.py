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

mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://botsin.space'
)
mastodon.log_in(
    MASTODON_USERNAME,
    MASTODON_PASSWORD,
    to_file = 'pytooter_usercred.secret'
)

mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://botsin.space'
)


api = tweepy.API(auth)

while True :
    g = blague(10)
    api.update_status(g)
    mastodon.status_post(g)
    print("Tweeting : ", g, " at ", asctime(localtime(time())))
    sleep(7200)
