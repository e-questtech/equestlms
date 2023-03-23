#!/bin/bash

# Activate the virtual environment
source /opt/render/project/src/venv/bin/activate

# Start Gunicorn
exec gunicorn config.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 4 \
  --timeout 120 \
  --log-level=info \
  --access-logfile - \
  --error-logfile -
