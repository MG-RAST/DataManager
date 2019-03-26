#!/bin/sh
set -e

if [ "$1" = 'start' ]; then
    exec python3 manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'migrate' ]; then
    exec python3 manage.py migrate
fi

exec "$@"