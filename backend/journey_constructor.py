import json
from config import init_users_db, init_journeys_db
from copy import deepcopy

def main(user, journeys_coll):
    #init_users_db()
    #init_journeys_db()
    #user=get_userdata() 
    full_data = construct(user, journeys_coll)
    return full_data


def get_journey(journeyname, journeys_coll):
    #json_data=open('../json_mocks/journey.json').read()
    #jdata=json.loads(json_data)
    jdata = journeys_coll.find_one({'journey': journeyname})
    return jdata


def construct(user, journeys_coll):
    #start new object with the user data
    full_data=deepcopy(user)
    #remove the existing journey list
    full_data["journeys"]=[]
    for j in user["journeys"]:
        full_data["journeys"].append(get_journey(j, journeys_coll))
    return full_data

def write_full(full_data):
    
    return "complete"
