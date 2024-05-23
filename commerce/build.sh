#!/bin/bash

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Compile static files (if applicable)
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Optionally, run tests
# python manage.py test

# Deactivate the virtual environment
# deactivate
