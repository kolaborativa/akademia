# -*- coding: utf-8 -*-
from pymongo import Connection

class Question(object):
    
    def __init__(self):
        global db 
        global mongo
        mongo = Connection('mongodb://akademia-dev:akademia-dev@paulo.mongohq.com:10084/akademia')
        db = mongo['akademia']
   
    def get_latest_questions(questions_title):
        questions = db.questions.find().limit(5)
        for questions in questions:
            questions_title = questions['title']
        return questions_title
