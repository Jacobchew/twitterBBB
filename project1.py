import os,re, math

from flask import Flask, render_template, request ,url_for
import jacobfunc

app = Flask(__name__)

@app.route('/sexyitems')
def things():
	return render_template('things.html')
@app.route('/')
def index():
	listoftweets = jacobfunc.jinbanyakmain()
	tweet = listoftweets['statuses']
	return render_template('index.html', data=tweet)	
	
if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 2002))
	app.run(host='127.0.0.1', port=port) 