#!/bin/sh
set -e

WARNING=<<EOF
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                *  Warning: Danger  *                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                       #
#   Enabling Django-extensions runserver_plus debugger  #
#   allows the execution of arbitrary code.             #
#                                                       #
#   Do not enable except for local developement. Set    #
#   DEBUG='OVERRIDE' to continue.                       #
#                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
EOF

DJANGO_HOST=${DJANGO_HOST:-"0.0.0.0"}
DJANGO_PORT=${DJANGO_PORT:-8000}

DBHOST=${DBHOST:-"postgresql"}
DBPORT=${DBPORT:-"5432"}

WAIT_FOR="wait-for $DBHOST:$DBPORT --"
START_CMD="runserver $DJANGO_HOST:$DJANGO_PORT"

if [ "$1" = "start" ]; then

    if [ -n $DEBUG ]; then
        if [ "$DJANGO_HOST" = "0.0.0.0" ] && [ "$DEBUG" != "OVERRIDE" ]; then
            START_CMD="runserver_plus $DJANGO_HOST:$DJANGO_PORT --reloader-interval 5"
        else
            echo $WARNING; exit -1;
        fi
    fi

    exec $WAIT_FOR python3 manage.py $START_CMD

elif [ "$1" = "manage" ]; then
    shift
    exec $WAIT_FOR python3 manage.py $@
fi

exec "$@"