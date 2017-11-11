from {{ cookiecutter.project_name }}.settings.base import *


ENVIRONMENT = 'test'
TESTING = True
MONGODB_SETTINGS['DB'] = '{{ cookiecutter.project_name }}-unit-tests'
