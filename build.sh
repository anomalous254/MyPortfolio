#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt
pip install --upgrade pip

python3 manage.py collectstatic --no-input
python3 manage.py migrate
