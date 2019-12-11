#!/bin/bash

set -e

pip install -r requirements-docker.txt
python src/manage.py migrate
python src/manage.py loaddata --format yaml fixtures.yaml
python src/manage.py collectstatic --noinput
cd src && gunicorn -c gunicorn.conf.py -p gunicorn-{{cookiecutter.project_name}}.pid config.wsgi
