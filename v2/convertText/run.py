from flask import Flask, request, jsonify 
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route("/convert", methods=["POST"])
def convert():
	data = request.get_json()
	print(data)
	
	text = data["text"]
	#text = data.get("text")
	return jsonify({"text": text})	

if __name__ == "__main__":
	app.run(debug=True)
