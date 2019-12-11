"""
Django settings for tjccconfig project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import datetime
import os

import raven

from . import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_uh0jj8&ge&xp_0^*n&ms_@)72pzlmx99-=4!7#esgdiq@%&#k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.TJHB_DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    '{{cookiecutter.project_slug}}',
    'kronos',

    'raven.contrib.django.raven_compat',

    'django_extensions',
    'django_filters',

    'rest_framework',
    'rest_framework.authtoken',

    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'whitenoise.runserver_nostatic',

    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.footer',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

USE_L10N = True
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3
from django.conf.locale.zh_Hans import formats

formats.NUMBER_GROUPING = 3

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'EXCEPTION_HANDLER': 'config.exception_handler.exception_handler',
}

JWT_AUTH = {
    # 'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.auth.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 60 * 24)
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost',
    'http://127.0.0.1',
)

# debug tool bar settings
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

import django.test.runner


# 单元测试不创建测试数据库
class MyTestRunner(django.test.runner.DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass


TEST_RUNNER = 'config.settings.MyTestRunner'

FOOTER = "Copyright &copy; 2002-2019 北京太极华保科技股份有限公司 版权所有 (京ICP备09058794号)"
MEDIA_URL = '/public/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
FILE_UPLOAD_PERMISSIONS = 0o644

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/cache_{{ cookiecutter.project_slug }}',
    }
}

# noinspection PyBroadException
try:
    release = raven.fetch_git_sha(BASE_DIR)
except:
    release = "0.1"

# raven config
RAVEN_CONFIG = {
    'dsn': '{{cookiecutter.sentry_dsn}}',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': release,
}

# Use telegraf to monitor your app health.
TELEGRAF_HOST = 'telegraf'
TELEGRAF_PORT = 8094
TELEGRAF_TAGS = {}
