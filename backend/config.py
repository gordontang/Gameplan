from flask import Flask
from flask.ext.pymongo import PyMongo

def init_users_db(app):
    app.config['MONGO1_HOST'] = 'ec2-54-167-222-78.compute-1.amazonaws.com'
    app.config['MONGO1_PORT'] = 27017
    app.config['MONGO1_DBNAME'] = 'users'
    mongo = PyMongo(app, config_prefix='MONGO1')
    return mongo

def init_journeys_db(app):
    app.config['MONGO2_HOST'] = 'ec2-54-167-222-78.compute-1.amazonaws.com'
    app.config['MONGO2_PORT'] = 27017
    app.config['MONGO2_DBNAME'] = 'journeys'
    mongo = PyMongo(app, config_prefix='MONGO2')
    return mongo

