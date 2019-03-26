import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '1q+1hce++u&uhek_)f2c7xju%e&(e^0a&9_2i&w*1_ej7+5ivh'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

# App settings
WSGI_APPLICATION = 'DataManager.wsgi.application'


auxdb_url = "postgresql://datamanager-auxdb@auxdb:26257?sslmode=disable"

DATABASES = {
    'default': { # PGSQL
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maindb',
        'USER': 'www_user',
        'PASSWORD': 'www_passwrd',
        'HOST': 'db',
        'PORT': 5432,
    },
    'auxdb': { # CockroachDB
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'datamanager_auxdb',
        'USER': 'datamanager_user',
        'HOST': 'auxdb',
        'PORT': 26257,
    }
} 

INSTALLED_APPS = [
    # Library Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'guardian',
    'rest_framework',
    'notifications',

    # Our Apps
    'DataManager.DataManagerAppConfig',
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
)

ROOT_URLCONF = 'DataManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    # Read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

validators = ['UserAttributeSimilarityValidator', 'MinimumLengthValidator',
                'CommonPasswordValidator', 'NumericPasswordValidator']
AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.%s' % v} for v in validators]

CELERY_TASK_ALWAYS_EAGER = True
NOTIFICATIONS_CHANNELS = {
    'console': 'notifications.channels.ConsoleChannel'
}

NOTIFICATIONS_USE_WEBSOCKET = True
NOTIFICATIONS_RABBIT_MQ_URL = 'message-bus'