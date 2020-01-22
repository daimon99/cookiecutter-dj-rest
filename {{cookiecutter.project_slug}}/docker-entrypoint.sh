#!/bin/bash
#
# Socialhome Docker Development entrypoint

# Exit immediately if a command exits with a non-zero status.
set -e

CODE_DIR=/data/prd/{{cookiecutter.project_slug}}

cd $CODE_DIR

# Define help message
show_help() {
    echo """
Usage: docker run <imagename> COMMAND
Commands
runserver      : Run Django development server
bash           : Start a bash shell
manage         : Run a Django management command
python         : Run a python command
shell          : Start a Django Python shell
celery         : Start celery worker
help           : Show this message
"""
}

# Run
case "$1" in
    runserver)
        echo "Running Development Server..."
        pip3 install -r requirements-docker.txt
        python3 src/manage.py migrate || (python3 cli.py fail; exit 1)
        python3 src/manage.py loaddata --format yaml fixtures.yaml
        python3 src/manage.py collectstatic --noinput
        python3 cli.py ok
        PYTHONPATH=./src gunicorn -c src/gunicorn.conf.py -p gunicorn-{{cookiecutter.project_slug}}.pid config.wsgi
    ;;
    bash)
        /bin/bash "${@:2}"
    ;;
    manage)
        pwd
        echo "Running manage:" "${@:2}"
        python3 src/manage.py "${@:2}"
    ;;
    python)
        echo "Running python command..." "${@:2}"
        python3 "${@:2}"
    ;;
    shell)
        echo "Running shell_plus..."
        python3 src/manage.py shell_plus
    ;;
    celery)
        echo "Running celery tasks..."
        cd src && celery -A config worker -l info
    ;;
    *)
        show_help
    ;;
esac
