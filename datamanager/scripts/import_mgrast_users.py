#!/bin/env python

from datamanager.ppo import User as WebAppUser
from datamanager.models import UserSerializer

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

import logging
logger = logging.getLogger(__name__)


def import_users(dryrun=False):
    '''
    WebApp User fields:
        _id, login, firstname, lastname, email, email2, password, comment, entry_date, active

    Django User fields:
        id, username, first_name, last_name, email, password, groups, user_permissions,
        is_staff, is_active, is_superuser, last_login, date_joined
    '''
    to_json = JSONRenderer().render

    for u in WebAppUser.objects.all():
        if u.password:
            kwargs={
                "username": u.login,
                "first_name": u.firstname,
                "last_name": u.lastname,
                "email": u.email,
                "password": u.password,
                "date_joined": u.entry_date,
                "is_active": u.active,
            }
            user = User(**kwargs)
            
            if dryrun:
                logger.info(to_json(data=UserSerializer(user).data).decode())
            else:
                try:
                    user.save()
                except:
                    logger.exception('Error attempting to save new user.')
                    continue

def run(*script_args):
    '''
    usage: manage runscript import_mgrast_user [--script-args='SCRIPT_ARGS']

    Creates new django.contrib.auth.User's from MG-RAST WebAppBackend db Users table.

    SCRIPT_ARGS:
        --dryrun        Logs json objects to 'INFO'. Does not write to db.
    '''

    dryrun = False
    if '--dryrun' in script_args:
        dryrun = True

    try:
        import_users(dryrun=dryrun)
    except:
        logger.exception('import_users - error')
