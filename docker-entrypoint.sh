#!/bin/bash
./wait_for_it.sh proxyserver:8000 -- echo "Proxyserver is up."

# Start server
./manage.py makemigrations
./manage.py migrate
echo "Starting server"
./manage.py runserver 0.0.0.0:8000
