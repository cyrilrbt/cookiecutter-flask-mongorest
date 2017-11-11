import mongoengine as db
import cleancat as cc
from flask import current_app as app
from {{ cookiecutter.project_name }}.documents import {{ cookiecutter.project_name|title }}Document


class User({{ cookiecutter.project_name|title }}Document):
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    roles = db.ListField(db.StringField(), default=['user'])

    def set_password(self, password):
        self.password = app.bcrypt.generate_password_hash(password).decode('utf-8')

    def test_password(self, password):
        return app.bcrypt.check_password_hash(self.password, password)

    def has_roles(self, *roles):
        return len(set(roles) & set(self.roles)) > 0

class UserSchema(cc.Schema):
    email = cc.Email(required=True)
    password = cc.String(required=False, default='')
    roles = cc.List(cc.String(), required=False, default=[])
