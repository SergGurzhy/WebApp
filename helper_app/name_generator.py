from flask import Flask, jsonify
from faker import Faker

fake = Faker()


app = Flask(__name__)


@app.route('/api/get_name', methods=['GET'])
def get_name():
    random_name = fake.name()
    return jsonify({'name': random_name})


@app.route('/', methods=['GET'])
def index():
    return 'Name generator v1.0.0'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
