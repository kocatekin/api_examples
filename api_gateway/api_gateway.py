from flask import Flask, jsonify
import requests as req
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute","2 per day"])


services = {}
services["dog"] = "http://localhost:5002/dog"
services["cat"] = "http://localhost:5001/cat"


@app.route('/api/v1/dog')
@limiter.limit("1 per minute")
def dog():
	res = req.get(services['dog'])
	return jsonify(res.json())

@app.route('/api/v1/cat')
def cat():
	res = req.get(services['cat'])
	return jsonify(res.json())

if __name__ == "__main__":
	app.run(port=8080, debug=True)
