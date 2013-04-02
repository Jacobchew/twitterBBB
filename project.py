import os ,re,math

from flask import Flask, request, url_for, render_template
import jacobfunc

app = Flask(__name__)

@app.route('/')
def index():
	listoftweets = jacobfunc.jinbanyakmain()
	tweets = listoftweets
	return render_template('index.html', data = tweets)

@app.route('/biscuit/')
def things():
	return render_template('things.html')	



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '127.0.0.1', port = port)
    

