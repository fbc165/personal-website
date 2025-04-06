#!/bin/bash

python billing/manage.py migrate

python billing/manage.py runserver 0.0.0.0:8000
