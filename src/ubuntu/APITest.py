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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
