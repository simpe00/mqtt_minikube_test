import os
import pytest
from ubuntu import main as umain

####################################
# https://realpython.com/python-testing/#how-to-structure-a-simple-test
####################################


# need to test without CORES!!! --> comment out ""@cross_origin()""
def test_hello():
    assert isinstance(umain.hello(), str) is True
    assert (umain.hello() == 'Hello world!') is True


def test_environment():
    assert isinstance(umain.environment(), str) is True


def test_health():
    assert isinstance(umain.health(), str) is True
