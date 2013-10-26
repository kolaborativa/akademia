# -*- coding: utf-8 -*-
from project import app
from project.models.Question import Question
from flask import render_template, request
from flask.ext.wtf import Form, TextField, validators
from pymongo import Connection

@app.route('/')
def start():
    questions = Question()
    questions = questions.get_latest_questions()
    return render_template('default/index.html',questions = questions)

@app.route('/question/<id>')
def question(id):
    question = Question()
    question = question.get_question_with_id(id)
    return render_template('default/question.html',question = question, id = id)
