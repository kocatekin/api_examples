from flask import Flask, jsonify
import requests as req

app = Flask(__name__)

@app.route('/cat')
def cat():
	res = req.get("https://api.thecatapi.com/v1/images/search")
	return jsonify(res.json())



if __name__ == "__main__":
	app.run(port=5001, debug=True)


