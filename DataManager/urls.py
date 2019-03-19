from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .models import UserViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]