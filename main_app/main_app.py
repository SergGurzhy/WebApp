import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
NAME_GEN = '/api/get_name'

# Используем переменную окружения для настройки URL вспомогательного сервиса
helper_app_url = os.getenv('HELPER_APP_URL', 'http://helper-app:5000')  # По умолчанию для docker-compose


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
        name = r.json()
        return name
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
