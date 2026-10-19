# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager

# config import
from config import app_config, app_active

# extensões compartilhadas do SQLAlchemy e do Flask-Mail
from extensions import db, mail

# controllers
from controller.User import UserController

# Importação necessária apenas para o Alembic enxergar essa tabela
from model.EventoPedido import EventoPedido

from admin.Admin import start_views
from flask_bootstrap import Bootstrap

# blueprints
from routes.main import main_bp
from routes.api import api_bp

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    mail.init_app(app)
    start_views(app, db)
    Bootstrap(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @login_manager.user_loader
    def load_user(user_id):
        user = UserController()
        return user.get_admin_login(user_id)

    return app
