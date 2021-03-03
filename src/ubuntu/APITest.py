# !flask/bin/python
from flask import Flask
import json
import os


app = Flask(__name__)


# Hello world endpoint
@app.route('/')
def hello():
    return 'Hello world!'


# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


# Get environment details
@app.route('/environment')
def environment():
    environment_data = {
        'hostname': os.getenv('HOSTNAME'),
        'PWD': os.getenv('PWD')
    }
    return json.dumps(environment_data)


# Verify the status of the microservice
@app.route('/test')
def test():
    return '{ "Var" : "Value" }'


# Verify the status of the microservice
@app.route('/test1')
def test1():
    return '{ "Var1" : "Value1" }'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
