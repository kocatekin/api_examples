from flask import Flask, jsonify, request
import requests as req
import random


app = Flask(__name__)


@app.route('/')
def index():
   return jsonify({"message":"hello from dog api"})


@app.route('/random')
def random_dog():
   res = req.get("https://dog.ceo/api/breeds/image/random")
   result = res.json()
   return jsonify({"url":result['message']}),200

@app.route('/breed/<name>')
def get_by_breed(name):
   res = req.get(f"https://dog.ceo/api/breed/{name}/images")
   result = res.json()
   all_images = result["message"]
   rnd_image = random.choice(all_images)
   return jsonify({"url":rnd_image}),200

   


if __name__ == "__main__":
   app.run(port=5001, debug=True)