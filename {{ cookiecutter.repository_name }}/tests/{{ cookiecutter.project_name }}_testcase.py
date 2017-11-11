import os
from flask_testing import TestCase

os.environ['{{ cookiecutter.project_name|upper }}_SETTINGS'] = '{{ cookiecutter.project_name }}.settings.test'

from {{ cookiecutter.project_name }}.main import app, settings
from {{ cookiecutter.project_name }}.auth import jwt_for

class BaseTestCase(TestCase):
    def setUp(self):
        self.assertEqual(settings.ENVIRONMENT, 'test')

    def tearDown(self):
        with self.app.app_context():
            self.app.db.connection.drop_database(settings.MONGODB_SETTINGS['DB'])

    def create_app(self):
        return app

    def add_user(self, email, password, roles=None):
        with self.app.app_context():
            from {{ cookiecutter.project_name }}.auth.documents import User
            u = User(email=email)
            if roles:
                u.roles = roles
            u.set_password(password)
            u.save()
            t = jwt_for(u)
            return u, t
