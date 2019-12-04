from flask import Flask, render_template, request, redirect, session, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_URI'] ='mongodb://reco:reco1234@localhost:27017/reco'
mongo = PyMongo(app)
#@app.route('/login', methods = ['POST', 'GET'])
#def login():
#		if request.method == 'POST':
			#session['username'] = request.form['username']
			#session['pass'] = request.form['pass']
# id ="ID"
# id = "pass"

 

if __name__ == '__main__':
    app.run(debug = True)