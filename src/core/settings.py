from pathlib import Path
import os
import os
import environ
from dotenv import load_dotenv

env = environ.Env(
    DEBUG=(bool, False)
)


BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"
}

SECRET_KEY = "django-insecure-gg6m%eokw*oomnl$x7aid%abt(vfpo&reoj3vv1&8po=_yj%yt"

DEBUG = True

ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'apps.clients',
    'apps.booking',
    'apps.tickets',
    'apps.main',

    # packages

    'rest_framework',
    "rest_framework.authtoken",
    'drf_spectacular',
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'), 
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', 
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'SkyFruMobile API',
    'DESCRIPTION': 'project description pass',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


AUTH_USER_MODEL = 'clients.User'


EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))


CORS_ALLOWED_ORIGINS = [
    "https://skyfru.kg",
    "https://www.skyfru.kg",
    "http://localhost:3000",
    "http://localhost:3001",
]


CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

DATABASES = {
    'default': env.db(),
}

NIKITA_LOGIN = os.getenv("NITKITA_LOGIN")
NIKITA_PASSWORD = os.getenv("NITKITA_PASSWORD")
NIKITA_SENDER = os.getenv("NITKITA_SENDER")


CORS_ALLOWED_ALL_ORIGINS = True

CSRF_TRUSTED_ALL_ORIGINS = True

CORS_ALLOW_ALL_HEADERS = True

CORS_ALLOW_METHODS = ("GET", "OPTIONS", "PATCH", "POST", "PUT", "DELETE")

USE_DJANGO_JQUERY = True

CELERY_BROKER_URL = 'redis://redis:6379/0'