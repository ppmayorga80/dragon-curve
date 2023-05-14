#!/bin/bash
# Copyright (c) 2021-present Divinia, Inc.

echo "                    __  "
echo " _   _  __ _ _ __  / _| "
echo "| | | |/ _' | '_ \| |_  "
echo "| |_| | (_| | |_) |  _| "
echo " \__, |\__,_| .__/|_|   "
echo " |___/      |_|         "
echo "                        "



if [[ "$*" == *"--apply"* ]]; then
  yapf -ir dragon_curve tests
  echo "Done"
else
  yapf -r --diff dragon_curve tests
  if [[ $? == 0 ]]; then
      echo "OK"
  else
      echo "yapf: to format, execute previous command with --apply flag"
  fi
fi

