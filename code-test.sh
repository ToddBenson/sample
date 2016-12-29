#!/bin/bash

pylint -r y $1
py.test tests/*_tests.py --cov=$1
