from flask import Flask, jsonify, render_template, request, url_for
from flask.ext.pymongo import PyMongo
from config import init_users_db, init_journeys_db
import json

app = Flask(__name__) 
from crossdomain import crossdomain

@crossdomain(origin='*')
def hello_world():
        print('asdf')
        return 'Hello, World!'

@app.route('/new_user', methods=['POST'])
@crossdomain(origin='*')
def create_user():
    user = {k: request.form[k] for k in request.form}
    #new_user = json.load('user_profile_template.json')
    #new_user['survey_results'] = survey_results
    user['journeys'] = []
    print user
    i_results = users_db.db.info.insert_one(user)
    return "Success"

@app.route('/create_user')
@crossdomain(origin='*')
def user_form():
    return render_template('add_user_form.html')

@app.route('/journeys', methods=['GET'])
@crossdomain(origin='*')
def get_all_journeys():
    journeys = list(journeys_db.db.test.find())
    for entry in journeys:
        entry.pop('_id')
    return jsonify(journeys)

@app.route('/assigned_journey', methods=['POST'])
@crossdomain(origin='*')
def add_journey():
    username = request.form['user_name']
    journeyname = request.form['journey_name']
    journey = journeys_db.db.test.find_one({'journey': journeyname})
    
    users_db.db.journey.update( {'user': username}
                         , {'$push': {'journeys': { "journey": journeyname
                                                  , "steps": journey['steps']
                                                  , "complete": False
                           }}}
                         )

@app.route('/assign_journey')
@crossdomain(origin='*')
def journey_form():
    return render_template('journey_form.html')

@app.route('/user_journey/<user_id>', methods=['GET'])
@crossdomain(origin='*')
def get_user(user_id):
    journey = users_db.db.journey.find_one_or_404({'user': user_id})
    #null check
    journey.pop('_id')
    print journey
    result = json.dumps(journey)
    return result

@app.route('/user/steve', methods=['GET'])
@crossdomain(origin='*')
def get__test_user():
    print("in steve")
    json_data=open('../json_mocks/user_w_journey.json').read()    
    print json_data
    return json_data

@app.route('/update_journey_status', methods=['POST'])
@crossdomain(origin='*')
def update_user_status():
    user_id = request.form['user_id']
    user_status = request.form['status']
    mongo.db.users.replace_one({'_id': user_id}, user_status)

if __name__ == "__main__":
    users_db=init_users_db(app)
    journeys_db=init_journeys_db(app)
    app.run(host='0.0.0.0',port=27020, debug=True)

