#import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
NAME_GEN = '/api/get_name'

# helper_app_url = os.getenv('HELPER_APP_URL', 'http://localhost:5001')
helper_app_url = 'http://helper_app:5000'


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


@app.route('/', methods=['GET'])
def index():
    return 'Main page'


@app.route('/api/random', methods=['GET'])
def get_random_name():

    r = requests.get(url=helper_app_url + NAME_GEN)
    if r.status_code == 200:
        name = r.text
        return name
    return "Start your name service"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
