#!/usr/bin/sh

# Get migration name
read -r -p "Enter migration name: " name
echo "Migration name: $name"

# Run alembic command inside the container
docker exec backend sh -c "cd src/database && alembic revision --autogenerate -m '$name'"
