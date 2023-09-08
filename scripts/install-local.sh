#!/usr/bin/sh

# Creates venv for project for local development testing alternative to docker

if [ ! -d venv ]; then
    echo "Creating venv"
    python3 -m venv venv
fi

echo "Installing dependencies"
venv/bin/pip install -r requirements/base.txt
venv/bin/pip install -r requirements/dev.txt
