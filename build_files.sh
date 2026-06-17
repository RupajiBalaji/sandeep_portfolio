#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
cd myportfolio
python manage.py collectstatic --noinput

# Run migrations (requires DATABASE_URL to be set in Vercel env vars)
python manage.py migrate --noinput
