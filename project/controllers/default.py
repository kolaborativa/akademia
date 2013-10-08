# -*- coding: utf-8 -*-
from project import app
from project.models.Question import Question
from flask import render_template, request
from flask.ext.wtf import Form, TextField, validators
from pymongo import Connection

@app.route('/')
def start():
    questions = Question()
    questions_title = questions.get_latest_questions()
    return render_template('default/index.html',questions_title = questions_title)

