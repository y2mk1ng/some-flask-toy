import flask
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

def create_app():
    return app

@app.route('/render/name', methods = ['POST'])
def render_it():
    parser.add_argument('Name', type = str)
    args = parser.parse_args()
    return args

app.run('0.0.0.0')
