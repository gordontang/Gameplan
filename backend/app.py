from flask import Flask, jsonify, render_template, request, url_for
from flask.ext.pymongo import PyMongo
from config import init_users_db, init_journeys_db
import json
import urllib2
from datetime import datetime
import journey_constructor
import ast

app = Flask(__name__) 
from crossdomain import crossdomain

@crossdomain(origin='*')
def hello_world(): 
        return 'Hello, World!'

@app.route('/new_user', methods=['POST'])
@crossdomain(origin='*')
def create_user():
    # insert user
    #user = {k: request.form[k] for k in request.form}   
    user = request.form.keys()[0]
    user = ast.literal_eval(user)
    print user 
   
    i_results = users_db.db.info.insert_one(user)     
    
    full_data = journey_constructor.main(user, journeys_db.db.journeys)
    #send user record with journey data to mongo
    i_results = users_db.db.journey.insert_one(full_data)
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

@app.route('/get_journey/<journeyname>', methods=['GET'])
@crossdomain(origin='*')
def get_journey(journeyname):
    journey=journeys_db.db.test.find_one_or_404({'journey':journeyname})
    journey.pop('_id')
    return jsonify(journey)

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
def get_user_journey(user_id):
    print user_id
    journey = users_db.db.journey.find_one_or_404({'email': user_id})
    #null check
    print 'j'
    print journey
    journey.pop('_id')
    print journey
    result = json.dumps(journey)
    return jsonify(result)

@app.route('/user/<user_name>', methods=['GET'])
@crossdomain(origin='*')
def get_user(user_name):
    user = users_db.db.info.find_one_or_404({'user': user_name})
    user.pop('_id')
    print user
    return json.dumps(user)

#@app.route('/update_journey_status', methods=['POST'])
@app.route('/update_user_journey/<user_name>/<journey_id>/<flag>', methods=['GET'])
@crossdomain(origin='*')
def update_user_status(user_name, journey_id, flag):
    user_journey = users_db.db.journey.\
                     find_one_or_404({'user': user_name,
                                      'journeys' : {"$elemMatch": {'journey':journey_id}}})
    user_journey.pop('_id')
    ix = 0
    while ix < len(user_journey['journeys']):
        if user_journey['journeys'][ix]['journey'] == journey_id:
            break
        ix += 1

    if 'journey_completed' in user_journey['journeys'][ix]:
        return "Journey already completed!"

    step_ix = user_journey['journeys'][ix]['current_step']
    dt = str(datetime.now())
    user_journey['journeys'][ix]['steps'][step_ix]['complete'] = dt.split(' ')[0]
    user_journey['journeys'][ix]['current_step'] += 1

    if user_journey['journeys'][ix]['current_step'] == len(user_journey['journeys'][ix]['steps']):
        user_journey['journeys'][ix]['journey_completed'] = True

    rec_id = users_db.db.journey.update({'user': user_name}, user_journey)
    return "success"

if __name__ == "__main__":
    users_db=init_users_db(app)
    journeys_db=init_journeys_db(app)
    app.run(host='0.0.0.0',port=27021, threaded=True, debug=True)
