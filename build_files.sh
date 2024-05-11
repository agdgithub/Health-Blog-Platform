#!/bin/bash

# Install Python 3.10
sudo apt update
sudo apt install python3.10

# Install dependencies
pip install -r requirements.txt

# Run collectstatic
python3.10 manage.py collectstatic
