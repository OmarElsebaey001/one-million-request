#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput


# Start server
echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 --workers 4 --threads 2 asset_project.wsgi:application