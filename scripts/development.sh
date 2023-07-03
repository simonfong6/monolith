#!/usr/bin/env bash
# Usage:
# Start the development environment.
# ./scripts/development.sh up
# Stop the development environment.
# ./scripts/development.sh down
docker-compose \
  -f docker-compose.development.yml \
  "$@"
