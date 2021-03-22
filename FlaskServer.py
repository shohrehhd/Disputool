from flask import Flask
from flask import request

app = flask.Flask(__name__)

@app.route('/hello', methods =['POST'])

def index():

	name =request.get_json()['name']
	return "Hello"+name

