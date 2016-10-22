from flask import Flask
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/add_survey', methods=['POST'])
def add_sign_in_survey():
    pass

@app.route('/sign_in_survey', methods=['GET'])
def get_sign_in_survey():
    survey = mongo.db.survey.find().sort('upload_date', PyMongo.DESCENDING)[0]
    return survey

@app.route('/create_new_user', methods=['POST'])
def create_user(user_key):
    survey_results = request.form['survey_results']

    new_user = json.load('user_profile_template.json')
    new_user['survey_results'] = survey_results
    new_user['journeys'] = []

    i_results = mongo.db.users.insert_one(new_user)
    return i_results.inserted_id


@app.route('/journeys', methods=['GET'])
def get_all_journeys():
    journeys = mongo.db.journeys.find()
    return journeys

@app.route('/journeys', methods=['POST'])
def upload_journey():
    pass

@app.route('/add_journey_user', methods=['POST'])
def add_journey_user():
    user_id = request.form['user_id']
    journey_id = request.form['journey_id']

    journey = mongo.db.journeys.find_one({'_id': journey_id})
    mongo.db.users.update( {'_id': user_id}
                         , {'$push': {'journeys': { "journey": journey
                                                  , "complete": False
                           }}}
                         )

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    #null check
    return user

@app.route('/update_journey_status', methods=['POST'])
def update_user_status():
    user_id = request.form['user_id']
    user_status = request.form['status']

    mongo.db.users.replace_one({'_id': user_id}, user_status)
