# ../flask/bin/python2.7

import tweepy
from app import app, db
from app.models import Match
import datetime
import requests
from multiprocessing import Pool

class WCGauge():

    def __init__(self):
        self.pool = Pool(processes=1)

