# coding: utf-8
import pytest

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
