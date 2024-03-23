import pymssql
from datetime import date
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from altin_json import main


app = Flask(__name__)
cors = CORS(app) #enable cors for everything - so the frontend can call


@app.route("/")
def index():
    my_dict = main()
    return my_dict

@app.route("/altin")
def altin():
    my_dict = main()
    return my_dict["gold"]

@app.route("/gumus")
def gumus():
    my_dict = main()
    return my_dict["silver"]

@app.route("/coupled")
def coupled():
	return "we will have a coupled app here"




if __name__ == "__main__":
    app.run(debug=True)
