# -*- coding: utf-8 -*-
from flask import Flask

# config import
from config import app_config, app_active

config = app_config[app_active]
def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return 'Hello World!'

    return app