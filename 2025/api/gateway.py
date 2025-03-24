from flask import Flask, jsonify, request
import requests as req


app = Flask(__name__)

#base url for services
CAT_SERVICE_URL = "http://localhost:5002"
DOG_SERVICE_URL = "http://localhost:5001"


@app.route('/')
def index():
   return jsonify({"message":"hello from the api gateway"}),200

@app.route('/cat')
def cat_service():
   res = req.get(CAT_SERVICE_URL)
   return jsonify(res.json()),200


#for dog

@app.route('/dog/<path:path>')
def dog_service(path):
   service_url = f"{DOG_SERVICE_URL}/{path}"
   res = req.get(service_url)
   return jsonify(res.json()),200

if __name__ == "__main__":
   app.run(port=5000, debug=True)