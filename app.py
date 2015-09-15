#!/Users/lawrence/anaconda/bin/python
import tweepy, sys, time, datetime

with open('/Users/lawrence/Documents/twitter_bot/keys.pass', 'r') as keys:
    CONSUMER_KEY = keys.readline().split(':')[1].strip('\n')
    CONSUMER_SECRET = keys.readline().split(':')[1].strip('\n')
    ACCESS_KEY = keys.readline().split(':')[1].strip('\n')
    ACCESS_SECRET = keys.readline().split(':')[1].strip('\n')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

begin_day =  datetime.date(2015, 9, 8)
today = datetime.date.today()
date_delta = today - begin_day
num_days = date_delta.days

with open('/Users/lawrence/Downloads/derby/bible.txt', 'r') as bible:
    status_text = bible.readlines()[num_days]
    api.update_status(status = status_text)

print 'test'