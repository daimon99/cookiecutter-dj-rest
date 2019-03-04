# coding: utf-8
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db.example.com',
        'NAME': 'external_db',
    }
