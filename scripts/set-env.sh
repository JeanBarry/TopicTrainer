#!/usr/bin/sh

# Creates .env file if it does not exists from .env.example

if [ ! -f .env ]; then
    echo "Creating .env file"
    cp .env.example .env
fi
