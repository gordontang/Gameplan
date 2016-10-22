from flask import Flask
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGOD_HOST'] = 'ec2-54-167-222-78.compute-1.amazonaws.com'
app.config['MONGOD_PORT'] = 27017
app.config['MONGOD_DBNAME'] = 'users'
mongo = PyMongo(app, config_prefix='MONGOD')

@app.route('/')
def hello_world():
        print('asdf')
        return 'Hello, World!'

@app.route('/new_user', methods=['POST'])
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

@app.route('/add_journey', methods=['POST'])
def add_journey():
    user_id = request.form['user_id']
    journey_id = request.form['journey_id']

    journey = mongo.db.journeys.find_one({'_id': journey_id})
    mongo.db.users.update( {'_id': user_id}
                         , {'$push': {'journeys': { "journey": journey
                                                  , "complete": False
                           }}}
                         )

@app.route('/user_journey/<user_id>', methods=['GET'])
def get_user_journey(user_id):
    journey = mongo.db.journey.find_one_or_404({'user': user_id})
    #null check
    journey.pop('_id')
    result = json.dumps(journey)
    return result

@app.route('/user/steve', methods=['GET'])
def get__test_user():
    print("in steve")
    json_data=open('../json_mocks/user_w_journey.json').read()    
    print json_data
    return json_data

@app.route('/update_journey_status', methods=['POST'])
def update_user_status():
    user_id = request.form['user_id']
    user_status = request.form['status']
    mongo.db.users.replace_one({'_id': user_id}, user_status)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=27020, debug=True)

