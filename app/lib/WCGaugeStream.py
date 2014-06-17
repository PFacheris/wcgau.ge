# ../flask/bin/python2.7

import tweepy
from app import app, db
from app.models import Match
import datetime
import requests
from app.config.keys import *

class WCGaugeStream():

    def __init__(self):
        self.startStream()

    def startStream(self):
        WCGaugeAuth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_SECRET_KEY)
        WCGaugeAuth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        class StreamListener(tweepy.StreamListener):
            def on_status(self, tweet):
                print tweet

            def on_error(self, status_code):
                print 'Error: ' + repr(status_code)
                return False


        l = StreamListener()
        self.streamer = tweepy.Stream(auth=WCGaugeAuth, listener=l)
        #setTerms = ['hello', 'goodbye', 'goodnight', 'good morning']
        setTerms = ['world cup', 'world cup 2014', 'worldcup', 'worldcup2014']
        self.streamer.filter(track=setTerms, async=True)

    def stopStream(self):
        self.streamer.disconnect()