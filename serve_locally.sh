#!/bin/bash
set -euo pipefail

DOCKER_COMPOSE_FILE="docker-compose-development.yml"

run_docker_compose() {
  echo "Starting setup..."
  docker compose -f $DOCKER_COMPOSE_FILE up -d
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

run_docker_compose
start_http_server
