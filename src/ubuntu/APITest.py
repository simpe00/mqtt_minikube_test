# !flask/bin/python
from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os
import platform
import main


app = Flask(__name__)
cors = CORS(app)                             # needed for swaggerUI extension
app.config['CORS_HEADERS'] = 'Content-Type'  # needed for swaggerUI extension


# Hello world endpoint
@app.route('/')
@cross_origin()                              # needed for swaggerUI extension
def hello():
    a = main.main() + 16
    return 'Hello world! '+str(a)


# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


# Get environment details
@app.route('/environment')
def environment():
    environment_data = {
        'hostname': os.getenv('HOSTNAME'),
        'system': platform.system(),
        'Version': platform.version(),
        'release': platform.release()
    }
    return json.dumps(environment_data)


# test
@app.route('/test')
def test():
    return '{ "Var" : "Value" }'


# test 1
@app.route('/test1')
def test1():
    return '{ "Var1" : "Value1" }'


if __name__ == '__main__':
    app.run(host='172.20.0.6', port=80)
