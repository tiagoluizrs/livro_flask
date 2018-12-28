# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# config import
from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    migrate = Migrate(app, db)

    db.init_app(app)

    @app.route('/')
    def index():
        return 'Meu primeiro run'

    @app.route('/login')
    def login():
        return 'Aqui entrará a tela de login'
    
    @app.route('/recovery-password')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'

    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']

        return 'Essa rota possui um método POST e criará um usuário com os dados de usuário %s e senha %s' % (username, password)
    
    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']
        
        return 'Essa rota possui um método PUT e editará o nome do usuário para %s e a senha para %s' % (username, password)
    
    return app