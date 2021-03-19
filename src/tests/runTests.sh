#!/bin/bash
TEMP_PATH="$PWD"
TEST_PATH="$(dirname $(readlink -f $0))"
cd "${TEST_PATH}/../"

coverage run -m pytest
coverage report -m
coverage html

# move files
mv "${TEST_PATH}/../htmlcov" "${TEST_PATH}/htmlcov"
mv "${TEST_PATH}/../.coverage" "${TEST_PATH}/.coverage"

cd "${TEMP_PATH}"