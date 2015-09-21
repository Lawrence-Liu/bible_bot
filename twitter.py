from flask import Flask, redirect, session, render_template, request, url_for
import tweepy
import os
app = Flask(__name__)

with open('/Users/lawrence/bible_bot/keys.pass', 'r') as keys:
    CONSUMER_KEY = keys.readline().split(':')[1].strip('\n')
    CONSUMER_SECRET = keys.readline().split(':')[1].strip('\n')

session = dict()
db = dict()
app = Flask(__name__)
#callback_url = 'https://dry-badlands-7049.herokuapp.com/verify'

@app.route('/')
def send_token():
    print 'Hello'
    redirect_url = ""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback=callback_url)
    try: 
        #get the request tokens
        redirect_url= auth.get_authorization_url()
        session['request_token'] = auth.request_token
    except tweepy.TweepError:
        print 'Error! Failed to get request token'
    return redirect(redirect_url)


@app.route('/verify')
def verify():
    verifier = request.args['oauth_verifier']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    token = session['request_token']
    del session['request_token']

    auth.request_token = token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'
    api = tweepy.API(auth)
    db['api']=api
    db['access_token_key']=auth.access_token
    db['access_token_secret']=auth.access_token_secret
    return redirect(url_for('index'))

@app.route("/index")
def index():
    #auth done, app logic can begin
    api = db['api']
    return api.user_timeline()
    #example, print your latest status posts
    #return render_template('tweets.html', tweets=api.user_timeline())

if __name__ == "__main__":
	port  = int(os.environ.get("PORT", 5000))
	callback_url = 'https://dry-badlands-7049.herokuapp.com/' + str(port) + 'verify'

	app.run(host = '0.0.0.0', port = port )

