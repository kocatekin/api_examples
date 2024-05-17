from flask import Flask, jsonify
import requests as req

app = Flask(__name__)

@app.route('/dog')
def dog():
	res = req.get("https://dog.ceo/api/breeds/image/random")
	return jsonify(res.json())

if __name__ == "__main__":
	app.run(port=5002, debug=True)
