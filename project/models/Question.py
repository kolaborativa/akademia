# -*- coding: utf-8 -*-
from pymongo import Connection
from pymongo import *
from operator import itemgetter
from bson.objectid import ObjectId

class Question(object):
    
    def __init__(self):
        global db 
        global mongo
        mongo = Connection('mongodb://akademia-dev:akademia-dev@paulo.mongohq.com:10084/akademia')
        db = mongo['akademia']
   
    def get_latest_questions(questions):
        questions = db.questions.find({}).limit(5)
        return questions

    def get_question_with_id(self,id):
        print(id)
        print(type(id))
        question = db.questions.find_one({"_id":ObjectId(id)})
        print(type(question))
        return question
