from flask import Flask, request, session, url_for
import os
app = Flask(__name__)

@app.route('/')
def homepage():
	return 'Hello, world'

@app.route('/about')
def about():
	return 'Lawrence'

if __name__ == "__main__":
	port  = int(os.environ.get("PORT", 5000)
	app.run(host = '0.0.0.0', port = port )