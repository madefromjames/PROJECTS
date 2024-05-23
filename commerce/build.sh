#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Create superuser if not exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists(): \
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" | python manage.py shell

# Run the server
gunicorn commerce.wsgi
