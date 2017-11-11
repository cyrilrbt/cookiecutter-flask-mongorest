from flask_mongorest.resources import Resource
from {{ cookiecutter.project_name }}.auth.documents import User, UserSchema
from {{ cookiecutter.project_name }}.auth import jwt_for


class SimpleUserResource(Resource):
    document = User
    fields = ['id', 'email']


class RegistrationUserResource(Resource):
    document = User
    fields = ['id', 'email', 'token']

    def token(self, obj):
        return jwt_for(obj)


class UserResource(Resource):
    document = User
    schema = UserSchema
    fields = ['id', 'email', 'roles']
    allowed_ordering = ['email']
