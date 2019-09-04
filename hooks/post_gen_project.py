# coding: utf-8
import sys, os, subprocess

project_slug = '{{cookiecutter.project_slug}}'

subprocess.getoutput(f'cp src/config/config.example.py src/config/config.py')

sys.exit(0)