from flask import Flask, jsonify
import requests as req

app = Flask(__name__)

SERVERS = ["http://localhost:5001","http://localhost:5002","http://localhost:5003"]

current_server_idx = 0

def get_next_server():
  global current_server_idx
  current_server_idx = (current_server_idx + 1) % len(SERVERS)
  return current_server_idx


@app.route('/')
def index():
  res = req.get(SERVERS[get_next_server()])
  return res.json()


if __name__ == "__main__":
  app.run(port=5000)
  
