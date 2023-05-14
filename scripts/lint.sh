#!/bin/bash
# Copyright (c) 2021-present Divinia, Inc.

echo "             _ _       _     "
echo " _ __  _   _| (_)_ __ | |_   "
echo "| '_ \| | | | | | '_ \| __|  "
echo "| |_) | |_| | | | | | | |_   "
echo "| .__/ \__, |_|_|_| |_|\__|  "
echo "|_|    |___/                 "



#W0703: too broad Exception
#R1721: tqdm(iterator)
#C3001: lambda functions
#C0301: line too long
#R0913: too many arguments
#R0914: too many local variables
#R0902: too many instance attributes
#R0801: similar lines in two or more files
#C0415: import outside toplevel (somehow when testing
#                                `aiohttp_requests` fails if put import as usual
#                                 the only solution is to put import inside the testing function)
DISABLE="W0703,R1721,C3001,C0301,R0913,R0914,R0902,R0801,C0415"

THRESHOLD="10.0"
PROJECT_DIR="dragon_curve/"
TEST_DIR="tests/"

pylint --disable=${DISABLE} \
  --variable-rgx='[a-z0-9_]+$' \
  --argument-rgx='[a-z0-9_]+$' \
  --fail-under=${THRESHOLD} \
  --recursive=y \
  --docstring-min-length 10 \
  ${PROJECT_DIR} ${TEST_DIR}

ERROR_CODE=$?
if [[ ${ERROR_CODE} != 0 ]]; then
  echo >&2 "pylint doesn't pass, ERROR_CODE=${ERROR_CODE}"
  exit ${ERROR_CODE}
fi
