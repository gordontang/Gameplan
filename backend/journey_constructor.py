import json
from config import init_users_db, init_journeys_db
from copy import deepcopy

def main():
    #init_users_db()
    #init_journeys_db()
    user=get_userdata() 
    full_data = construct(user)
    return full_data

def get_userdata():
    json_data=open('../json_mocks/user.json').read()
    userdata=json.loads(json_data)
    return userdata

def get_journey(journey):
    json_data=open('../json_mocks/journey.json').read()
    jdata=json.loads(json_data)
    return jdata


def construct(user):
    #start new object with the user data
    full_data=deepcopy(user)
    #remove the existing journey list
    full_data["journeys"]=[]
    for j in user["journeys"]:
        full_data["journeys"].append(get_journey(j))
    return full_data

def write_full(full_data):
    
    return "complete"
