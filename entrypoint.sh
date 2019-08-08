#!/bin/sh

cd /app
pipenv install --system --deploy
pipenv run flask run --host=0.0.0.0
