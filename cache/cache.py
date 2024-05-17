from flask import Flask, request, jsonify
import time

app = Flask(__name__)

cache = {}

def get_from_cache(key):
	return cache.get(key, None)

def set_in_cache(key, value):
	cache[key] = value

def check_cache(key):
	if key in cache:
		value = cache[key]
		return value
	return None


@app.route('/data/<id>')
def get_data(id):
	key = id
	cached_data = check_cache(key)
	if cached_data:
		return jsonify({"data": cached_data, "from_cache": True})

	time.sleep(2)
	data = "here is some data"
	set_in_cache(key, data)
	return jsonify({"data": data, "from_cache": False})

if __name__ == "__main__":
	app.run(debug=True)
