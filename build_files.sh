#!/bin/bash

mkvirtualenv --python=/usr/bin/python3.10 venv

pip install -r requirements.txt

python manage.py collectstatic
