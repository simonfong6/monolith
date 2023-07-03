#!/usr/bin/env bash
PROJECT_NAME="template-flask-react_test"
DOCKER_COMPOSE_FILE="docker-compose.test.yml"

docker-compose \
  -f $DOCKER_COMPOSE_FILE \
  -p $PROJECT_NAME \
  up \
    --abort-on-container-exit\
    --exit-code-from api \

code=$?

docker-compose \
  -f $DOCKER_COMPOSE_FILE \
  -p $PROJECT_NAME \
  down

exit $code
