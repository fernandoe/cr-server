#!/bin/bash

# Build the project
echo "Building the project..."
# python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
# TODO: Uncomments when add support to the database
# python3.9 manage.py makemigrations --noinput
# python3.9 manage.py migrate --noinput

echo "Collect Static..."
# TODO Uncomment when add suport to the database
# python3.9 manage.py collectstatic --noinput --clear
