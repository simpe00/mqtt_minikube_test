import os
import pytest
import json
from flask import session
from pyserver import main as umain

####################################
# https://realpython.com/python-testing/#how-to-structure-a-simple-test
####################################


@pytest.fixture
def client():
    with umain.app.test_client() as client:
        yield client


# need to test without CORES!!! --> comment out ""@cross_origin()""
def test_hello(client):
    response = client.get('/')
    assert (response.data == b'Hello world!') is True


@pytest.mark.parametrize(('model'), (
    ('defaultModel'),
    ('model'),
))
def test_TEST(client, model):
    assert isinstance(model, str) is True
    # check get-Method
    response = client.get('/TEST/%s' % model)
    (response.status_code == 200) is True

    # check post-Method
    response = client.post(
        '/TEST/%s' % model,
        data=json.dumps(dict(
            Data1="A String for Data 1",
            Data2="A String for Data 2",
            Data3="A String for Data 3"
        )),
        content_type='application/json'
    )
    jsondata = json.loads(response.data.decode('utf8'))
    assert (jsondata['model'] == model) is True


@pytest.mark.parametrize(('indexname', 'filename'), (
    ('countryvaccinations', 'country_vaccinations.csv'),
    ('Test', 'Test')
))
def test_csv2elastic(client, indexname, filename):
    # check post-Method
    response = client.get(
        '/csv2elastic',
        query_string={'indexname': indexname, 'filename': filename}
    )
    jsondata = json.loads(response.data.decode('utf8'))

    if (indexname == 'Test'):
        assert (jsondata['status'] == 'ERROR') is True

    if (indexname == 'countryvaccinations'):
        assert (jsondata['status'] == 'DONE') is True


def test_environment(client):
    response = client.get('/environment')
    jsondata = json.loads(response.data.decode('utf8'))
    assert (jsondata['system'] == 'Linux') is True


def test_health(client):
    response = client.get('/health')
    jsondata = json.loads(response.data.decode('utf8'))
    assert (jsondata['status'] == 'UP') is True
