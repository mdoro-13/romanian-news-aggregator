#!/bin/bash
set -eo pipefail

DOCKER_COMPOSE_FILE="docker-compose-development.yml"

run_docker_compose() {
  echo "Starting setup..."
  if [[ $1 == "-build" ]]; then
    docker compose -f $DOCKER_COMPOSE_FILE up -d --build
  else
    docker compose -f $DOCKER_COMPOSE_FILE up -d
  fi
}

start_http_server() {
  cd UI
  echo "Starting HTTP server..."
  python -m http.server 5500 --bind 127.0.0.1
}

trap 'stop_docker_compose' INT

stop_docker_compose() {
  echo "Stopping local setup..."
  docker compose -f $DOCKER_COMPOSE_FILE down
  exit 0
}

if [[ $1 == "-build" ]]; then
  run_docker_compose "-build"
else
  run_docker_compose
fi

start_http_server
