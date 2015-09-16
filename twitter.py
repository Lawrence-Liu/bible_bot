from flask import Flask, request, session, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
	return 'Hello, world'


if __name__ == "__main__":
	app.run()