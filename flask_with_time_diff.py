import flask, time, celery
import flask_app
from flask import Flask
from flask_restful import Resource, Api, reqparse
from celery import Celery
from flask_app import create_app

def celerymake(flask_app):
    create_app.config['CELERY_ACCEPT_CONTENT'] = ['json']
    create_app.config['CELERY_TASK_SERIALIZER'] = 'json'
    create_app.config['CELERY_RESULT_SERIALIZER'] = 'json'
    create_app.config['CELERY_RESULT_BACKEND'] = '127.0.0.1:5000'
    create_app.config['CELERY_BROKER_URL'] = '127.0.0.1:5000'

    c = Celery(create_app.import_name,
            backend = '127.0.0.1:5000',
            broker = '127.0.0.1:5000',
            )
    c.conf.update(create_app.config)
