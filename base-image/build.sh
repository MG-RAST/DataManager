#!/bin/bash

DOCKERFILE="-f Dockerfile"
if  [ "$1" = 'offline' ]; then
    DOCKERFILE='-f Dockerfile-offline'
    shift
fi

IMAGE=${1:-'mgrast/django-base'}

echo "Building ${IMAGE} from ${DOCKERFILE}"

docker build -t ${IMAGE}:build ${DOCKERFILE} .
TAG=`docker images | grep ${IMAGE} | grep build | awk '{print $3}'`

# tag build and del previous 'latest'
docker tag ${IMAGE}:build ${IMAGE}:${TAG}
docker rmi ${IMAGE}:latest

# tag new build as latest and delete build
docker tag ${IMAGE}:${TAG} ${IMAGE}:latest
docker rmi ${IMAGE}:build