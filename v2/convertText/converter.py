from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from convertClass import Text


app = Flask(__name__)
cors = CORS(app)


@app.route('/convert', methods=['POST'])
def convert():
	data = request.get_json()
	text = data["text"]
	obj = Text(text)
	myDict = {}
	myDict["pascalcase"] = obj.pascalcase()
	myDict["camelcase"] = obj.camelcase()
	myDict["snakecase"] = obj.snakecase()
	myDict["kebabcase"] = obj.kebabcase()
	myDict["flatcase"] = obj.flatcase()
	myDict["traincase"] = obj.traincase()
	myDict["cobolcase"] = obj.cobolcase()
	return jsonify(myDict)	


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
