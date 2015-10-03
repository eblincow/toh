#!/usr/bin/env bash
# set -x
cp run-tests.sh .git/hooks/pre-commit
python tests.py

# is everything ok?


