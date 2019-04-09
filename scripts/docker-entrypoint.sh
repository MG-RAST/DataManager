#!/bin/sh
set -e

case $1 in
    "start" )
        wait-for-postgres.sh python manage.py $DJANGO_CMD ${DJANGO_HOST}:${DJANGO_PORT} $DJANGO_CMD_OPTIONS
        exit;;
    "manage" ) 
        shift; 
        wait-for-postgres.sh python3 manage.py $@
        exit;;
    "runscript" ) 
        shift
        if [ $# > 1 ]; then
            script=$1
            shift
            wait-for-postgres.sh python3 manage.py runscript $script --script-args="$@"
        else
            wait-for-postgres.sh python3 manage.py runscript $@
        fi
        exit;;
esac

exec "$@"