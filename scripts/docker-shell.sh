#!/usr/bin/sh

# Check if .env file exists before trying to use its content
if [ ! -f .env ]; then
    echo ".env file not found"
    exit 1
fi

#source .env file
. $(pwd)/.env

# Exec inside the container
docker exec -it -u "${UID}:${GID}" backend sh
