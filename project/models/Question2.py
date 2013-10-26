from mongoengine import *

class Question(object):
    def __init__(self):
        global db
        global mongo
        mongo = connect('akademia',host='mongodb://akademia-dev:akademia-dev@paulo.mongohq.com:10084/akademia')

    def get_question_qith_id2(id,question):
        question = Question.objects('id'=id)
        return question, id
