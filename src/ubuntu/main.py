# !flask/bin/python
from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os
import socket
import platform
from CSV2ELASTIC import csv2elastic as c2e


app = Flask(__name__)
cors = CORS(app)                             # needed for swaggerUI extension
app.config['CORS_HEADERS'] = 'Content-Type'  # needed for swaggerUI extension


# Hello world endpoint
@app.route('/')
@cross_origin()                              # needed for swaggerUI extension
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
        'system': platform.system(),
        'Version': platform.version(),
        'release': platform.release()
    }
    return json.dumps(environment_data)


# trigger read CSV to Elastic
@app.route('/csv2elastic')
def csv2elastic():
    c2e.main()
    return '{ "status" : "DONE" }'


if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()),
            port=int(os.getenv('PORT_API')))
