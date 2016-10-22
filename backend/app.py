from flask import Flask, jsonify
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def hello_world():
        print('asdf')
        return 'Hello, World!'

@app.route('/add_survey', methods=['POST'])
def add_sign_in_survey():
    pass

@app.route('/sign_up_survey', methods=['GET'])
def get_sign_up_survey():
    survey = mongo.db.survey.find().sort('upload_date', PyMongo.DESCENDING)[0]
    return jsonify(survey)

@app.route('/', methods=['POST'])
def get_user_id():
    user_name = request.form['name']
    user_email = request.form['email']

    user = mongo.db.users.find_one( {'name': user_name, 'email': user_email} )
    return user['_id']


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
    return jsonify(journeys)

@app.route('/journeys', methods=['POST'])
def upload_journey():
    journey = request.form['journey']

    result = mongo.db.journeys.insert(journey)
    return result.inserted_id

@app.route('/add_journey_user', methods=['POST'])
def add_journey_user():
    user_id = request.form['user_id']
    journey_id = request.form['journey_id']

    journey = mongo.db.journeys.find_one({'_id': journey_id})
    journey['complete'] = False
    mongo.db.users.update( {'_id': user_id}
                         , {'$push': {'journeys': journey
                           }}
                         )

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    #null check
    return jsonify(user)

@app.route('/user/steve', methods=['GET'])
def get__test_user():
    print("in steve")
    with open('../json_mocks/user_w_journey.json') as f:
        json_data = json.load(f)
    print json_data
    return jsonify(json_data)

@app.route('/update_journey_status', methods=['POST'])
def update_user_status():
    user_id = request.form['user_id']
    user_status = request.form['status']

    mongo.db.users.replace_one({'_id': user_id}, user_status)

if __name__ == "__main__":
    app.run()

