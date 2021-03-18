#!/bin/bash
TEMP_PATH="$PWD"
TEST_PATH="$(dirname $(readlink -f $0))"
cd "${TEST_PATH}/../"

coverage run -m pytest
coverage report -m
coverage html

cd "${TEMP_PATH}"