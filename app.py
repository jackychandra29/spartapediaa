from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.environ.get("mongodb+srv://???:sparta@cluster0.gaybq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("dbsparta")

client = MongoClient(MONGODB_URL)
db = client(DB_NAME)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST request!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)