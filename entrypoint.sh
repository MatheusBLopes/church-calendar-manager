#!/bin/bash

# Collect static files
python church-calendar-manager/manage.py collectstatic --no-input

# Start App
gunicorn -c gunicorn_config.py church_calendar_manager.wsgi:application
