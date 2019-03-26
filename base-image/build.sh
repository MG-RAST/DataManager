#!/bin/bash

docker build -t mgrast/django-base:latest .

# cleanup
#docker images | grep django-base | cut -f4 -d' ' | xargs -I{} echo "mgrast/django-base:"{} | xargs docker rmi
