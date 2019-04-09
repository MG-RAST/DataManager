import logging

import django.urls
from django.apps import AppConfig

logger = logging.getLogger(__name__)

_original_reverse = django.urls.reverse

def reverse_patch(viewname, **kwargs):
    if viewname[:15] == "filebrowser:fb_":
        viewname = "seqcenter:{}".format(viewname[15:])
    return _original_reverse(viewname, **kwargs)

django.urls.reverse = reverse_patch

class SeqCenterConfig(AppConfig):
    name = 'seqcenter'
