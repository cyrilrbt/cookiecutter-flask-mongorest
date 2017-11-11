import json
from setuptools import setup, find_packages


setup(
    name='{{ cookiecutter.project_name }}',
    version='0.0.1',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_name }} = {{ cookiecutter.project_name }}.main:main',
        ]},
)
