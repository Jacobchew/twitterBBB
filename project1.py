import os,re, math

from flask import Flask, render_template, request ,url_for
import jacobfunc

app = Flask(__name__)

@app.route('/sexyitems')
def things():
	return render_template('things.html')
dataAB =[]
@app.route('/')
def index():
	list = jacobfunc.jinbanyakmain()
	tweet = list['statuses']
	for afeez in range(5):
		dataAB[afeez] = tweet[afeez]['text']
	return render_template('index.html', data=tweet, lala=dataAB)	
	
if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 2002))
	app.run(host='127.0.0.1', port=port) 