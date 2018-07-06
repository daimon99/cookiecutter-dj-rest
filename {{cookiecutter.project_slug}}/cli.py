#!/usr/bin/env python
# coding: utf-8

import click
import subprocess


@click.group()
def main():
    pass


@main.command()
def mm():
    """make migration and migrate it."""
    click.secho('make migrations...', fg='yellow')
    subprocess.call('python src/manage.py makemigrations', shell=True)
    click.secho('migrate...', fg='yellow')
    subprocess.call('python src/manage.py migrate', shell=True)


if __name__ == '__main__':
    main()
