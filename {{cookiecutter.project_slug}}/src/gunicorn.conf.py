# coding: utf-8
import multiprocessing

bind = "127.0.0.1:{{cookiecutter.port}}"
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "info"
proc_name = "{{cookiecutter.project_slug}}"
worker_class = "gevent"
timeout = 300