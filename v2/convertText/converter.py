from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


def pascalcase(text):
	return ''.join([x.title() for x in text.split(" ")])

def camelcase(text):
	a = text.split(" ")
	return a+''.join([x.title() for x in a[1::])

def snakecase(text):
	return '_'.join([x for x in text.split(" ")])


@app.route('/index')
def index():
	return "hello world"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
