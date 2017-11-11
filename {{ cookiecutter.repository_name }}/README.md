# {{ cookiecutter.project_name }}

## Reading

- [Buildout](http://www.buildout.org)
- [Mongoengine](http://mongoengine.org/)
- [Flask-MongoRest](https://github.com/closeio/flask-mongorest)

## Running locally

This project uses [Buildout](http://www.buildout.org) for dependency management. Head over there to learn more about it, but here's the rundown:

* `python3 bootstrap.py` : Installs dependencies for `buildout` only needed the first time
* `bin/buildout` : Install our project's dependencies, reads `buildout.cfg` by default
* `vim {{ cookiecutter.project_name }}/settings/base.py` : Update the default (dev) settings for your environment
* `vim {{ cookiecutter.project_name }}/settings/test.py` : You may need to update the test settings
* `bin/nosetests` : Run all the unit tests
* `open cover/index.html` : Consult code coverage of the tests
* `bin/{{ cookiecutter.project_name }} runserver` : Finally start the app

At this point, the api is available at [http://localhost:8000/](http://localhost:8000/)

## Deploying on a server

### Environment files

Files for deploying to a server are included. It assumes a `production` environment and provides all required files for it:

* `production.cfg` : Buildout settings for production, in this case we only add a dependency on [gunicorn](http://gunicorn.org/)
* `{{ cookiecutter.project_name }}/settings/production.py` : App settings for the `production` environment
* `server_config/supervisord.conf` : A [supervisor](http://supervisord.org/) configuration for starting (and restarting in case something goes wrong) the backend.
* `server_config/nginx.conf` : An [nginx](https://www.nginx.com/) configuration for serving the backend.


### Deployment

Assuming a recent ubuntu server, and that you want to deploy in `/path/to/{{ cookiecutter.project_name }}`:

* `sudo apt-get install build-essential python3 python3-dev libffi-dev nginx supervisor mongodb` : Install system dependencies
* `cd /path/to` : Go in the target's parent directory
* `git clone ??? {{ cookiecutter.project_name }}` : Clone our project in the desired target
* `cd {{ cookiecutter.project_name }}`
* `python3 bootstrap.py` : Get buildout's dependencies
* `bin/buildout -c production.cfg` : Get our dependencies for `production`
* `cd ../`
* `sudo ln -s /path/to/{{ cookiecutter.project_name }}/server_config/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.project_name }}.conf` : Put our supervisor config in the right place
* `sudo service supervisor restart` : Make supervisor re-read its config to start our app
* `sudo ln -s /path/to/{{ cookiecutter.project_name }}/server_config/nginx-api.conf /etc/nginx/sites-enabled/{{ cookiecutter.project_name }}.conf` : Put our nginx config in the right place
* `sudo service nginx reload` : Make nginx re-read its config and make our app available
