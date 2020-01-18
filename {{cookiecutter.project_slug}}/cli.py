#!/usr/bin/env python
# coding: utf-8

import logging
import os
import subprocess
import sys

import click
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

log = logging.getLogger(__name__)


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


@main.command()
def ok():
    """通知服务ok"""
    # 发送启动通知
    import requests
    import socket
    from django.utils.timezone import now
    from django.conf import settings
    qywx_notice_key = "<robot key>"
    if qywx_notice_key != "<robot key>":
        requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=key',
            json={
                "msgtype": "text",
                "text": {
                    "content": f"{{cookiecutter.project_slug}} [{settings.VERSION}] 服务重启完成: {socket.gethostname()}, {now().astimezone()}"
                }})
    else:
        print("If you want to get a notice after deploy, please provide a key in the above.")


if __name__ == '__main__':
    main()
