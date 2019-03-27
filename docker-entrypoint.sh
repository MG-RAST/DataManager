#!/bin/sh
set -e

PORT=${DJANGO_PORT:-8000}

if [ "$1" = 'start' ]; then
    exec python3 manage.py runserver 0.0.0.0:${PORT}
elif [ "$1" = 'manage' ]; then
    shift
    exec python3 manage.py $@
fi

exec "$@"