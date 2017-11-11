import json

from tests.{{ cookiecutter.project_name }}_testcase import BaseTestCase


class AuthenticationTest(BaseTestCase):
    def test_auth_no_user(self):
        r = self.client.post(
            '/api/v0/authenticate/',
            data=json.dumps({'email': 'a@a.com', 'password': 'no'}),
            content_type='application/json'
        )
        self.assert_403(r)

    def test_auth(self):
        self.add_user('hello@hello.com', 'hello')
        r = self.client.post(
            '/api/v0/authenticate/',
            data=json.dumps({'email': 'hello@hello.com', 'password': 'hello'}),
            content_type='application/json'
        )
        self.assert_200(r)
        self.assertIn('token', r.json)

    def test_wrong_password(self):
        self.add_user('hello@hello.com', 'hello')
        r = self.client.post(
            '/api/v0/authenticate/',
            data=json.dumps({'email': 'hello@hello.com', 'password': 'wrong'}),
            content_type='application/json'
        )
        self.assert_403(r)

    def test_auth_required(self):
        r = self.client.get('/api/v0/identity/')
        self.assert_401(r)

    def test_invalid_token(self):
        r = self.client.get('/api/v0/identity/', headers={'Authorization': 'no'})
        self.assert_401(r)

    def test_register(self):
        r = self.client.post(
            '/api/v0/register/',
            data=json.dumps({'email': 'a@a.com', 'password': 'meow'}),
            content_type='application/json'
        )
        self.assert_200(r)
        data = r.json
        self.assertEqual(data['email'], 'a@a.com')

    def test_double_register(self):
        r = self.client.post(
            '/api/v0/register/',
            data=json.dumps({'email': 'a@a.com', 'password': 'meow'}),
            content_type='application/json'
        )
        self.assert_200(r)
        r = self.client.post(
            '/api/v0/register/',
            data=json.dumps({'email': 'a@a.com', 'password': 'meow'}),
            content_type='application/json'
        )
        self.assert_400(r)

    def test_incomplete_register(self):
        r = self.client.post(
            '/api/v0/register/',
            data=json.dumps({'email': 'a@a.com'}),
            content_type='application/json'
        )
        self.assert_400(r)
