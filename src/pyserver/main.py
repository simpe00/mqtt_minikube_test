# !flask/bin/python
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import os
import socket
import platform
from CSV2ELASTIC import csv2elastic as c2e
import logging


# looging for development
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s'
                    ' {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S',
                    filemode='w',
                    level=logging.INFO)


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()
cors = CORS(app)                             # needed for swaggerUI extension
app.config['CORS_HEADERS'] = 'Content-Type'  # needed for swaggerUI extension


# Hello world endpoint
@app.route('/')
# @cross_origin()                              # needed for swaggerUI extension
def hello():
    return 'Hello world!'


# Test args string
@app.route('/TEST/<model>',  methods=['GET', 'POST'])
def TEST(model):
    if request.method == 'GET':
        reqArgs = request.args
        return json.dumps(reqArgs)
    elif request.method == 'POST':
        t1 = request.json
        t1['model'] = model
        logging.info(t1)
        return json.dumps(t1)
    else:
        logging.info('try GET or POST method')
        return '{ "status" : "ERROR" }'


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
    indexname = request.args.get('indexname')
    filename = request.args.get('filename')

    try:
        c2e.main(indexname, filename)
        return '{ "status" : "DONE" }'
    except Exception:
        logging.error("file could not transferred to elastic")
        return '{ "status" : "ERROR" }'


if __name__ == '__main__':
    # run app / debug for calling reloader for hot-reload
    app.run(host=os.getenv('IPV4_ADRR'),
            port=int(os.getenv('PORT_API')),
            debug=True)
