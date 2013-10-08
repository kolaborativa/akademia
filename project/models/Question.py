# -*- coding: utf-8 -*-
from pymongo import Connection

class Question(object):
    
    def __init__(self):
        global db 
        global mongo
        mongo = Connection('mongodb://<user>:<password>@dharma.mongohq.com:10046/myapp')
        db = mongo['myapp']
   
    def get_latest_questions(questions_title):
        questions = db.questions.find().limit(5)
        for questions in questions:
            questions_title = questions['title']
        return questions_title
