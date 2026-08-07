#!/bin/bash
# Utility script to build RPMs in a Docker container and then install them

set -euo pipefail

TAG=$1
DOCKERFILE=$2

IMAGE=libcobblersignatures:$TAG

echo "==> Build container ..."
docker build -t "$IMAGE" -f "$DOCKERFILE" .

echo "==> Build RPMs ..."
mkdir -p rpm-build
# ":z" relabels the bind mount for container access on SELinux hosts; it's a
# no-op on hosts without SELinux.
docker run --rm -t -v "$PWD/rpm-build:/usr/src/libcobblersignatures/rpm-build:z" "$IMAGE"

echo "==> Start container ..."
docker run -t -d --name libcobblersignatures -v "$PWD/rpm-build:/usr/src/libcobblersignatures/rpm-build:z" "$IMAGE" /bin/bash

echo "==> Install fresh RPMs ..."
docker exec -t libcobblersignatures bash -c 'rpm -Uvh rpm-build/libcobblersignatures-*.noarch.rpm'

echo "==> Stop container ..."
docker stop libcobblersignatures
echo "==> Delete container ..."
docker rm libcobblersignatures
