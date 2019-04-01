#!/usr/bin/env python
import os
import sys
import time

from django.db.utils import OperationalError

import logging
logger = logging.getLogger()

attempts = os.environ.get("DJANGO_RETRY_ATTEMPTS", 5)
retry_delay = os.environ.get("DJANGO_RETRY_DELAY", 5)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datamanager.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    attempt = 1
    while attempt <= attempts:
        try:
            execute_from_command_line(sys.argv)
        except OperationalError:
            msg = "Attempt {} of {}: DB still starting up. Retrying in {} seconds."
            logger.info(msg.format(attempt, attempts, retry_delay))
            time.sleep(retry_delay)
        except SystemExit as exit_except:
            logger.debug('\n ####### Restarting Django ####### \n')
            attempt = 1
            raise exit_except

