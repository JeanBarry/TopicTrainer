#!/usr/bin/sh

# Removes all docker containers, images, volumes, networks and cache

docker container rm -f $(docker container ls -aq)
docker image rm -f $(docker image ls -aq)
docker volume rm -f $(docker volume ls -q)
docker network rm -f $(docker network ls -q)
docker system prune -f
