import os

# App settings model
WSGI_APPLICATION = 'DataManager.wsgi.application'
ROOT_URLCONF = 'DataManager.urls'

# Enviroment Override Settings
# --------------------------------------------------------------
# usage        names
# ------------ -------------------------------------------------
# default db : DBNAME, DBUSER, DBPASSWORD, DBHOST, DBPORT
# ------------ -------------------------------------------------
# roachdb    : ROACH_DBNAME, ROACH_USER, ROACH_DBPASSWORD,
#            : ROACH_DBHOST, ROACH_DBPORT
# ------------ -------------------------------------------------
# django     : DJANGO_DEBUG, DJANGO_BASE_DIR, DJANGO_SECRET_KEY, 
#            : DJANGO_PORT, DJANGO_ALLOWED_HOSTS
# ------------ -------------------------------------------------

# Alias environ getter for legiblity
env=os.environ.get

DJANGO_PORT = env('DJANGO_PORT')
ALLOWED_HOSTS = [env('DJANGO_ALLOWED_HOSTS', '*')]
DEBUG = env('DJANGO_DEBUG', True)
BASE_DIR = env('DJANGO_BASE_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = env('DJANGO_SECRET_KEY', '1q+1hce++u&uhek_)f2c7xju%e&(e^0a&9_2i&w*1_ej7+5ivh')

DATABASES = {
    # PGSQL Main db
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DBNAME', 'maindb'),
        'USER': env('DBUSER', 'www_user'),
        'PASSWORD': env('DBPASSWORD','www_passwrd'),
        'HOST': env('DBHOST','db'),
        'PORT': int(env('ROACH_DBPORT', 5432))
    },
    # CockroachDB
    # example connection url "postgresql://www_user@cockroachdb:26257?sslmode=disable"
    'roach': { 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('ROACH_DBNAME', 'roachdb'),
        'USER': env('ROACH_DBUSER', 'www_user'),
        'HOST': env('ROACH_DBHOST', 'roachdb'),
        'PORT': int(env('ROACH_DBPORT', 26257))
    }
}

# Internationalization settings
LANGUAGE_CODE, TIME_ZONE, STATIC_URL = 'en-us', 'UTC', '/static/'
USE_L10N = USE_I18N = USE_TZ = True

INSTALLED_APPS = [
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

TEMPLATES = [{
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

# Notify package settings
CELERY_TASK_ALWAYS_EAGER = True
NOTIFICATIONS_CHANNELS = {
    'console': 'notifications.channels.ConsoleChannel'
}

NOTIFICATIONS_USE_WEBSOCKET = True
NOTIFICATIONS_RABBIT_MQ_URL = 'message-bus'