#!/bin/bash
set -e

if [ ! -d "venv" ]; then
  echo "Creating virtualenv"
  virtualenv venv
fi
source venv/bin/activate

if [ -e "requirements.txt" ]; then
  echo "Installing requirements"
  pip install -r requirements.txt
fi

# echo "Linting!!!"
# flake8

if [ -e "manage.py" ]; then
  echo "Running migrations"
  python manage.py migrate

  echo "Running application"
  python manage.py runserver 0.0.0.0:8000
fi