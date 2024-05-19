import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
NAME_GEN = '/api/get_name'
helper_app_url = 'http://helper-app-service.default.svc.cluster.local:5000'  # Полное DNS-имя


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


@app.route('/', methods=['GET'])
def index():
    return 'Main page'


@app.route('/api/random', methods=['GET'])
def get_random_name():
    try:
        r = requests.get(url=helper_app_url + NAME_GEN)
        r.raise_for_status()
        name = r.json().get('name')
        return name
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
