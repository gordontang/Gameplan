from flask import Flask, jsonify, render_template, request, url_for
from flask.ext.pymongo import PyMongo
from config import init_users_db, init_journeys_db
import json

app = Flask(__name__) 
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
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
    return i_results.inserted_id

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

@app.route('/add_journey', methods=['POST'])
@crossdomain(origin='*')
def add_journey():
    username = request.form['user_id']
    journey_id = request.form['journey_id']
    journey = journeys_db.db.test.find_one({'_id': journey_id})
    users_db.db.journeys.update( {'user': username}
                         , {'$push': {'journeys': { "journey": journey
                                                  , "complete": False
                           }}}
                         )

@app.route('/create_journey')
@crossdomain(origin='*')
def journey_form():
    return render_template('journey_form.html')

@app.route('/user_journey/<user_id>', methods=['GET'])
@crossdomain(origin='*')
def get_user(user_id):
    journey = users_db.db.journey.find_one_or_404({'user': user_id})
    #null check
    journey.pop('_id')
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

