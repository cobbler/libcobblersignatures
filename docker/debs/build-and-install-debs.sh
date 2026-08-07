#!/bin/bash
# Utility script to build DEBs in a Docker container and then install them

set -euo pipefail

TAG=$1
DOCKERFILE=$2

IMAGE=libcobblersignatures:$TAG

echo "==> Build container ..."
docker build -t "$IMAGE" -f "$DOCKERFILE" .

echo "==> Build packages ..."
mkdir -p deb-build
# ":z" relabels the bind mount for container access on SELinux hosts; it's a
# no-op on hosts without SELinux.
docker run --rm -t -v "$PWD/deb-build:/usr/src/libcobblersignatures/deb-build:z" "$IMAGE"

echo "==> Start container ..."
docker run -t -d --name libcobblersignatures -v "$PWD/deb-build:/usr/src/libcobblersignatures/deb-build:z" "$IMAGE" /bin/bash

echo "==> Install fresh packages ..."
docker exec -t libcobblersignatures bash -c 'apt-get update -qq && apt-get install -qqy ./deb-build/libcobblersignatures*.deb'

echo "==> Stop container ..."
docker stop libcobblersignatures
echo "==> Delete container ..."
docker rm libcobblersignatures
