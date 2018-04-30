#!/bin/bash
./wait_for_it.sh proxyserver:8000 -- echo "Proxyserver is up."

# Start server
echo "Starting server"
./manage.py runserver 0.0.0.0:8000
