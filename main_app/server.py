import requests
from flask import Flask, jsonify

app = Flask(__name__)
URL_NAME_GEN = 'http://helper_app:5000/api/get_name'


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


@app.route('/', methods=['GET'])
def index():
    return 'Main page'


@app.route('/api/random', methods=['GET'])
def get_random_name():
    r = requests.get(url=URL_NAME_GEN)
    if r.status_code == 200:
        name = r.text
        return name
    return "Start your name service"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
