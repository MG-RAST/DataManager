from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from rest_framework import routers
from filebrowser.sites import site as fb_site
from seqcenter.sites import site

from .models import UserViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = [
    path('', site.urls),
    path('filebrowser/', fb_site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^accounts/', include('allauth.urls')),
    #url('^notifications/', include('notifications.urls', namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]