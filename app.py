#! /usr/bin/python3

import datetime
import random
import string
import requests

from fatsecret import Fatsecret

from datetime import date
from datetime import datetime
from functools import wraps

from flask import Flask
from flask import render_template, url_for, request, redirect, flash, json, jsonify, abort
from flask import session as user_session

#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)


# # # https://platform.fatsecret.com/ 
CLIENT_ID = '1440c913658946288210afe51060abb9'
CONSUMER_KEY = "36204616e82b44ba92bce8bc98319bfa"
CONSUMER_SECRET = "54d74afc01a848c9ac76b5293d8b7728"
fs = Fatsecret(CONSUMER_KEY, CONSUMER_SECRET)    
# # # REST API OAuth 2.0 Credentials  

# App routes
"""
Show Home function for the HomePage.
"""


@app.route('/', methods = ["GET", "POST"])
def index(): 
    title = default()
    return jsonify({200: title})

@app.route("/item/<food>")
def one_product_json(food):
    res=fetch_data(food)    
    return jsonify(res)    
    
    
@app.errorhandler(500)
def internal_error(error):        
    return "500 error %d",date.strftime()
 
def default():
    return 'welcome'

def fetch_data(item):
    food_value=fs.foods_search(item,1,1)    
    food_id = food_value['food_id']
    food_value=fs.food_get_v2(food_id)
    return food_value


# declaring a main function
if __name__ == "__main__":
    app.debug = True
    print("server running")         
    app.run()
    
    