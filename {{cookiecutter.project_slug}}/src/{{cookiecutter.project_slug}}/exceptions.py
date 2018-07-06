# coding: utf-8
from rest_framework.exceptions import APIException


class {{cookiecutter.project_slug.capitalize()}}Exception(APIException):
    pass
