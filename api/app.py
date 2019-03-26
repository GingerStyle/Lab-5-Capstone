from flask import Flask, g, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict

#create flask web app
flaskApp = Flask(__name__)
#create database
database = SqliteDatabase('chainsaw.db')

#create model class
class Chainsaw(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta():
        database = database

#create table to store chainsaw juggling records
database.create_tables([Chainsaw])

#handles what happens before a request is executed
@flaskApp.before_request
def before_request():
    g.db = database
    g.db.connect()

#handles what happens after a request is executed
@flaskApp.after_request
def after_request(response):
    g.db.close()
    return response

#gets all records
@flaskApp.route('api/chainsaw')
def get_all():
    #get all records
    result = Chainsaw.select()
    #convert result into json and store n dictionaries
    return jsonify([model_to_dict(x) for x in result])

#get one record with an id
@flaskApp.route('api/chainsaw/<catcher_id>')
def get_by_id(catcher_id):
    try:
        c = Chainsaw.get_by_id(catcher_id)
        return jsonify([model_to_dict(c)])
    except DoesNotExist:
        return 'Not found', 404


