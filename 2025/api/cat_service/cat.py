from flask import Flask, jsonify, request
import requests as req


app = Flask(__name__)


@app.route('/')
def index():
   return jsonify({"message":"hello from cat api"})


@app.route('/random')
def random_cat_picture():
   res = req.get("https://api.thecatapi.com/v1/images/search")
   result = res.json()
   return jsonify({"url":result[0]["url"]}),200


if __name__ == "__main__":
   app.run(port=5002, debug=True)