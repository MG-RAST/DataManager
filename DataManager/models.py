import uuid
import io

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import path

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser


# User model, serializer, and rest-framework viewsets classes
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ['url', 'password']


class UserViewSet(viewsets.ModelViewSet):
    '''
    /user/

    default actions:
    .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Type model, serializer, and rest-framework viewsets classes
class Type(models.Model):
    '''
    Contains jsonld description of a data type that can be validated and "blessed" for use within a project. 
    '''

    uuid = models.UUIDField('Immutable UUID4', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('Human readable name', max_length=30, unique=True, db_index=True)
    is_approved = models.BooleanField( default=False)
    createdt = models.DateTimeField('Creation datetime', auto_now_add=True)
    moddt = models.DateTimeField('Last modified datetime', auto_now=True)
    description = JSONField('JSONLD formated type description')
    metadata = JSONField('Key value metadata relating to type')

    def __str__(self):
        return "{} <{}>".format(self.name, self.uuid)


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    '''
    '''
    class Meta:
        model = Type
        fields = '__all__'


class TypeViewSet(viewsets.ModelViewSet):
    '''
    /type/

    default actions:
    .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()

    addional actions:
    .validate() - json post validated against jsonld type.description

    '''
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(detail=True, methods=['post'], name='Validate instance of Type',
            url_path='validate_type', url_name='validate-instance-of-type')
    def validated(self, request, pk=None):
        pass


# Helper functions
def create_type_from_json(json):
    data = JSONParser().parse(io.BytesIO(json))
    ts = TypeSerializer(data=data)
    if ts.is_valid():
        return ts.save()
    return ts.errors

# Register models w/ Admin
admin.site.register(Type)