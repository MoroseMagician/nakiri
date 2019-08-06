#!/bin/sh

cd /app
pipenv shell
flask db init --yes
flask run --host=0.0.0.0
