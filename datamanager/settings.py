import os

# App settings model
WSGI_APPLICATION = 'datamanager.apps.application'
ROOT_URLCONF = 'datamanager.urls'

# Alias environ getter for legiblity
env=os.environ.get

DJANGO_PORT = env('DJANGO_PORT')
ALLOWED_HOSTS = [env('DJANGO_ALLOWED_HOSTS')]

DEBUG = env('DJANGO_DEBUG')

SECRET_KEY = env('DJANGO_SECRET_KEY')
BASE_DIR = env('DJANGO_BASE_DIR')

# Main datamanager django db
psql_conf = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('POSTGRES_DB'),
    'USER': env('POSTGRES_USER'),
    'PASSWORD': env('POSTGRES_PASSWORD'),
    'HOST': env('POSTGRES_HOST'),
    'PORT': int(env('POSTGRES_PORT'))
}

# Experimental cockroach db:
# Currently unable to support Django required tables
# See: cockroachdb/cockroachdb-python/pull/14 for details
roach_conf = { 
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('ROACH_DB'),
    'USER': env('ROACH_USER'),
    'HOST': env('ROACH_HOST'),
    'PORT': int(env('ROACH_PORT'))
}

# Dump of WebAppBackend from MG-RAST
mgrast_dump_conf = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': env('MYSQL_DB'),
    'PASSWORD': env('MYSQL_PASSWORD'),
    'HOST': env('MYSQL_HOST'),
    'PORT': int(env('MYSQL_PORT'))
}

DATABASES = {
    'default': psql_conf,
    #'roach': roach_conf,
    #'WebAppBackend': mgrast_dump_conf,
}

# Internationalization settings
LANGUAGE_CODE, TIME_ZONE, STATIC_URL = 'en-us', 'UTC', '/static/'
USE_L10N = USE_I18N = USE_TZ = True

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'guardian',
    'rest_framework',
    'notifications',
    'datamanager.DataManagerConfig',
    'seqcenter.SeqCenterConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

MEDIA_ROOT = BASE_DIR + '/media'
STATIC_ROOT = MEDIA_ROOT + '/static'


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

# Django REST framework settings
REST_FRAMEWORK = {
    # Read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly']
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': validator} for validator in [
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'django.contrib.auth.password_validation.MinimumLengthValidator',
        'django.contrib.auth.password_validation.CommonPasswordValidator', 
        'django.contrib.auth.password_validation.NumericPasswordValidator'
    ]
]

SOCIALACCOUNT_PROVIDERS = {
    'openid': {
        'SERVERS': [
            dict(id='cilogin',
                 name='CILogin',
                 openid_url='https://cilogon.org/authorize'),
        ]
    }
}

# Notify package settings
#CELERY_TASK_ALWAYS_EAGER = True
#NOTIFICATIONS_CHANNELS = {'console': 'notifications.channels.ConsoleChannel'}

#NOTIFICATIONS_USE_WEBSOCKET = True
#NOTIFICATIONS_RABBIT_MQ_URL = 'message-bus'

LOGGING_CONFIG = None

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'datamanager': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'seqcenter': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
})

FILEBROWSER_DEFAULT_PERMISSIONS = None
FILEBROWSER_MAX_UPLOAD_SIZE = 10000000000
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_EXTENSIONS = {
    'Sequence': ['.fasta', '.fastq'],
    'File': ['.zip', 'tar.gz', '.dmg', '.dat'],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
}