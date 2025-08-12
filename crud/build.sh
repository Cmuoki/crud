#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input  # Only if using static files
python manage.py migrate                   # Only if using a database