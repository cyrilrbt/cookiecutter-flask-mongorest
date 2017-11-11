import os
import importlib
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_mongorest import MongoRest
from flask_cors import CORS
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


settings = importlib.import_module(os.environ.get('{{ cookiecutter.project_name|upper }}_SETTINGS', '{{ cookiecutter.project_name }}.settings.base'))
app = Flask(__name__)

app.url_map.strict_slashes = False
app.config.from_object(settings)

app.db = MongoEngine(app)
app.api = MongoRest(app)
app.bcrypt = Bcrypt(app)
app.cors = CORS(app)

# Load views
import {{ cookiecutter.project_name }}.auth.views

# Make all errors json
def make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response

for code in default_exceptions:
    app.errorhandler(code)(make_json_error)


def main():  # pragma: no cover
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
