from flask import Flask
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def hello_world():
        return 'Hello, World!'


@app.route('/new_user', methods=['POST'])
def create_user(user_key):
    survey_results = request.data

    new_user = json.load('user_profile_template.json')
    new_user['survey_results'] = survey_results
    new_user['journeys'] = []

    i_results = mongo.db.users.insert_one(new_user)
    return i_results.inserted_id


