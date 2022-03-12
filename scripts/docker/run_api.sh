#!/bin/sh

cd /api_usican/
rm /api_usican/db.sqlite3
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py loaddata seed/*.json
python manage.py runserver 0.0.0.0:8000
