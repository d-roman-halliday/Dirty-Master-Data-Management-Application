#!/bin/bash

# Inspired by:
# https://flask.palletsprojects.com/en/2.1.x/patterns/packages/

if [[ "$VIRTUAL_ENV" != "" ]]
then
  INVENV=1
else
  INVENV=0
fi

if [[ INVENV -eq 0 ]]
then
  source venv/bin/activate
fi

export FLASK_APP=dmdma
export FLASK_ENV=development

# Only needed the once
# pip install -e .

# Only needed the once
# flask init-db

flask run