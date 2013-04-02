import os,re, math

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/sexyiteams')
def things():
	return render_template('things.html')
	
if __name__=__main__:
	app.debug=True
	port = int(os.environ.get('PORT', 2002))
	app.run(host='126.0.0.1', port=port) 