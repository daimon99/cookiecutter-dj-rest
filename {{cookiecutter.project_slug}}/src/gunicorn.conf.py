# coding: utf-8

bind = "0.0.0.0:{{cookiecutter.port}}"
workers = 4
loglevel = "info"
proc_name = "{{cookiecutter.project_slug}}"
worker_class = "gevent"
timeout = 300
