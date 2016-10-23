from flask import Flask, jsonify, render_template, request, url_for
from flask.ext.pymongo import PyMongo
from config import init_users_db, init_journeys_db
import json

app = Flask(__name__) 
from crossdomain import crossdomain

@app.route('/insert_temp', methods=['GET'])
def insert_temp_user():
    with open('../json_mocks/user_w_journey.json') as f:
        json_data = json.load(f)
    print dict(json_data)
    users_db.db.journey.insert_one(dict(json_data))
    
    return jsonify(json_data)

@app.route('/brand_new_journey', methods=['GET','POST'])
@crossdomain(origin='*')
def new_journey_form():
    print request.form
    journey_name=request.form['journey_name']
    num_steps=(len(request.form)-1)/4
    steps=[]

    for i in range(1,num_steps+1):
        step={}
        step['type']=request.form['type' + str(i)]
        step['description']=request.form['desc' + str(i)]  
        step['link']=request.form['link' + str(i)]  
        step['points']=request.form['points' + str(i)]  
        steps.append(step)
    complete_record={'journey':journey_name, "steps":steps}
    
    journeys_db.db.test.insert_one(complete_record)
    return "success" 



@app.route('/new_user', methods=['POST'])
@crossdomain(origin='*')
def create_user():
    # insert user
    user = {k: request.form[k] for k in request.form}
    i_results = users_db.db.info.insert_one(user)
    # insert user journey
    user['journeys'] = []
    i_results = users_db.db.journey.insert_one(user)
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
def get_user(user_id):
    journey = users_db.db.journey.find_one_or_404({'user': user_id})
    #null check
    journey.pop('_id')
    print journey
    result = json.dumps(journey)
    return result

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

