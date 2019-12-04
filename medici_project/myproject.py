import os
import re
import random
import bson
import json
import subprocess
import time
#import datetime
import copy
import sys
from MDC.crawlering.crawler import youtube_crawler
#import MDC
from collections import Counter
from bson import json_util
from werkzeug import secure_filename
import numpy as np
import hashlib 	
#import requests
#import urllib.request #

#sys.path.append('/home/ubuntu/myproject')
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))



import pytz
from flask import Flask, render_template, request, redirect, session, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import flask
print(flask.__version__)


import pymongo
print(pymongo.__version__)
app = Flask(__name__)




app.config['MONGO_URI'] ='mongodb://reco:reco1234@localhost:27017/reco'
mongo = PyMongo(app)
print("1",mongo)
#result=mongo.db.users.find({}) 
#for i in result:
#    print(i)
#@app.route('/')
#@app.route('/index')
#def index():
#    result=mongo.db.user_test.find({})
#    return render_template('index.html')

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')
	
@app.route('/loginAction', methods = ['POST', 'GET'])

@app.route('/crawler_e', methods = ['POST', 'GET'])
def crawler_e():
	return render_template('crawler_e.html')
@app.route('/crawler', methods = ['POST', 'GET'])
def crawler():
	return render_template('crawler.html')
	
@app.route('/crawlering', methods=['POST', "GET"])
#input 으로 크롤링 받기
def crawlering(n_limit=20):
	if request.method == 'POST':
		search = request.form['keyword']
		data_list = youtube_crawler(search, n_limit=10)
		print("3",data_list)
		collection = mongo.db.crawler
		for d in data_list:
			collection.save({
				"keyword": search,
				"type": "youtube",
				"title": d['title'],
				"url": "https://www.youtube.com" + d['url'],
				"thumbnail": d['thumbnail'],
				"content": d['content'],
				"author": d['author'],
				"viewCount": d['viewCount'],
				"likeCount": d['likeCount'],
				"hateCount": d['hateCount']
				#"createdAt": isodate,
				#"updatedAt": isodate
			})
			return render_template('index.html')
	else:
		return render_template('crawler1.html')
		
    #, data=result, alert_msg=''
    
if __name__ == "__main___":
    app.debug = True
    app.run()
 #이거 안해도 실행이 되었던 이유 질문
