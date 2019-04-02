#!/usr/bin/env python
import os
import sys
import time

warning='''# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                *  Warning: Danger  *                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                       #
#   Enabling Django-extensions runserver_plus debugger  #
#   allows the execution of arbitrary code.             #
#                                                       #
#   Do not enable except for local developement.        #
#                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''

if __name__ == '__main__':

    #TODO
    # warn if runserver_plus w/ allowed host other than localhost

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datamanager.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

