#!/bin/sh

export FLASK_APP=./santa_maria/index.py

pipenv run flask --debug run -h localhost