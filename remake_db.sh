#!/bin/bash
rm db.sqlite3
pipenv run python manage.py migrate
pipenv run python manage.py loaddata api/fixtures/*.yaml