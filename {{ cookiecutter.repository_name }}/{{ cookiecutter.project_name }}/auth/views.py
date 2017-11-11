from flask import jsonify, abort, request
from flask_mongorest.views import ResourceView
from flask_mongorest.methods import List, Fetch, Create, Update, Delete
from {{ cookiecutter.project_name }}.main import app
from {{ cookiecutter.project_name }}.auth.documents import User
from {{ cookiecutter.project_name }}.auth import JwtAuthentication, jwt_for, current_user
from {{ cookiecutter.project_name }}.auth.resources import RegistrationUserResource, UserResource
import mongoengine


@app.route('/api/v0/authenticate/', methods=['POST'])
def authenticate():
    data = request.json
    try:
        user = User.objects.get(email=data.get('email'))
    except User.DoesNotExist:
        abort(403, 'Invalid credentials')
    if user.test_password(data.get('password')):
        token = jwt_for(user)
        return jsonify(token=token)
    abort(403, 'Invalid credentials')


@app.route('/api/v0/identity/', methods=['GET'])
def identity():
    user = current_user()
    if user:
        ur = UserResource()
        user.id = str(user.id)
        return jsonify(**ur.serialize(user))
    abort(401)


@app.api.register(url='/api/v0/register/')
class RegistrationView(ResourceView):
    resource = RegistrationUserResource
    methods = [Create]

    def has_add_permission(self, request, obj):
        obj.set_password(obj.password)
        obj.roles = []
        obj.save()
        return True

    def post(self, *args, **kwargs):
        try:
            return super().post(*args, **kwargs)
        except mongoengine.errors.NotUniqueError:
            abort(400, 'Account already exists')


# @app.api.register(url='/api/v0/users/')
# class UserView(ResourceView):
#     resource = UserResource
#     methods = [List, Fetch, Create, Update, Delete]
#     authentication_methods = [JwtAuthentication]

#     def has_read_permission(self, request, qs):
#         user = current_user()
#         if user.has_roles('user_manager', 'admin'):
#             return qs
#         return qs.filter(id=user.id)

#     def has_change_permission(self, request, obj):
#         user = current_user()
#         if user.has_roles('user_manager', 'admin') or obj.id == user.id:
#             return True
#         return False

#     def has_delete_permission(self, request, obj):
#         user = current_user()
#         return user.has_roles('user_manager', 'admin')

#     def has_add_permission(self, request, obj):
#         user = current_user()
#         if user.has_roles('user_manager', 'admin'):
#             obj.set_password(obj.password)
#             obj.save()
#             return True
#         return False

#     def put(self, **kwargs):
#         # Due to an inconsistency in flask-mongorest,
#         # we can't update the password in the has_change_permission
#         # callback like we can for creation.
#         pk = kwargs.get('pk')
#         r = super().put(**kwargs)
#         if pk:
#             try:
#                 u = User.objects.get(id=pk)
#             except User.DoesNotExist:
#                 pass
#             else:
#                 u.set_password(u.password)
#                 u.save()
#         return r
