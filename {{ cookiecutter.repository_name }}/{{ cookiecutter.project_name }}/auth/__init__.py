import datetime
import jwt
from flask import request
from {{ cookiecutter.project_name }}.auth.documents import User
from flask_mongorest.authentication import AuthenticationBase


def jwt_for(user):
    from {{ cookiecutter.project_name }}.main import settings
    e = datetime.datetime.utcnow() + settings.JWT_EXPIRATION
    return jwt.encode({
        'email': user.email,
        'exp': e
    }, settings.JWT_SECRET).decode('utf-8')


def current_user():
    from {{ cookiecutter.project_name }}.main import settings
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization'].split(' ')[1]
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
            if datetime.datetime.fromtimestamp(data['exp']) >= datetime.datetime.utcnow():
                return User.objects.get(email=data['email'])
        except:
            pass


class JwtAuthentication(AuthenticationBase):
    def authorized(self):
        return current_user()
