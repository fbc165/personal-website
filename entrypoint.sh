#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn website.wsgi:application --bind 0.0.0.0:8000 --workers 5 --timeout 120
