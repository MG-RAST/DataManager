import logging
from functools import partial

from django.contrib.auth import urls as auth
from django.core.files.storage import FileSystemStorage, default_storage
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from filebrowser.decorators import file_exists, path_exists
from filebrowser.sites import FileBrowserSite

from .storage import ShockStorage

logger = logging.getLogger(__name__)


class SeqCenterBrowser(FileBrowserSite):

    def __init__(self, name='seqcenter', app_name='seqcenter', storage=default_storage):
        super().__init__(name, app_name, storage)

    def get_urls(self):
        from django.conf.urls import url

        # filebrowser urls (views)
        urlpatterns = [
            url(r'^$', self.index, name="index"),
            url(r'^account/', self.user_account, name="user_account"),
            url(r'^claim/$', self.claim_view, name="claim"),
            url(r'^browse/$', path_exists(self, never_cache(self.browse)), name="browse"),
            url(r'^createdir/', path_exists(self, never_cache(self.createdir)), name="createdir"),
            url(r'^upload/', path_exists(self, never_cache(self.upload)), name="upload"),
            url(r'^delete_confirm/$', file_exists(self, path_exists(self, never_cache(self.delete_confirm))), name="delete_confirm"),
            url(r'^delete/$', file_exists(self, path_exists(self, never_cache(self.delete))), name="delete"),
            url(r'^detail/', file_exists(self, path_exists(self, never_cache(self.detail))), name="detail"),
            url(r'^version/$', file_exists(self, path_exists(self, never_cache(self.version))), name="version"),
            url(r'^upload_file/$', csrf_exempt(self._upload_file), name="do_upload"),
        ]

        urlpatterns += auth.urlpatterns

        return urlpatterns

    def index(self, request):
        return render(request, "seqcenter/index.html", {
            'next': request.GET.get('next', '/seqcenter/claim')
        })

    def user_account(self, request):
        # django.contrib.auth.forms PasswordChangeForm
        return render(request, "seqcenter/user_account.html", {})

    def claim_view(self, request):
        return render(request, 'seqcenter/claim.html', {})


site = SeqCenterBrowser(storage = ShockStorage(url='http://shock:7445'))