#!/bin/bash/env sh

echo "Migrations"
python manage.py migrate --noinput

echo "Run server"
python manage.py runserver 0.0.0.0:8000