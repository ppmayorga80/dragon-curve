#!/bin/bash

echo "             _            _   "
echo " _ __  _   _| |_ ___  ___| |_ "
echo "| '_ \| | | | __/ _ \/ __| __|"
echo "| |_) | |_| | ||  __/\__ \ |_ "
echo "| .__/ \__, |\__\___||___/\__|"
echo "|_|    |___/                  "



#1. set the test coverage value and other shell variables
COVERAGE_THRESHOLD="90"
PROJECT_DIR="dragon_curve"
TEST_DIR="tests"

#2. execute the test coverage command
# for test the "io" directory under project dir, execute the following
#           bash test.sh io
# this will cause that pytest will executed with the following arguments
#           --cov=dai_proc/io tests/io
#
# for testing everything, execute this script without arguments
#           bash test.sh
#
# take care if you want to test a single file, because pytest
# will test a single file within a directory and then, if there
# are another files within the directory, this will cause unexpected results
# Example: the following command to test a jsonl program:
#           bash test.sh io/test_jsonl.py
# will execute pytest with the following arguments
#           --cov=dai_proc/io tests/io/test_jsonl.py
# and, pass test_jsonl.py but detects another files under dai_proc/io that aren't covered
# causing unexpected results...
#
# Summary: execute this script without arguments or provide a single argument with a directory name!

COV_DIR="${PROJECT_DIR}/$*"
PROCESS_TEST_DIR_OR_FILE="${TEST_DIR}/$*"

if [[ -f "${PROCESS_TEST_DIR_OR_FILE}" ]]; then
  COV_DIR=${PROJECT_DIR}/$(dirname "$@")
fi

pytest --cov-report term-missing:skip-covered \
  --timeout=30 \
  --cov-fail-under=${COVERAGE_THRESHOLD} \
  --cov=${COV_DIR} \
  "${PROCESS_TEST_DIR_OR_FILE}"
