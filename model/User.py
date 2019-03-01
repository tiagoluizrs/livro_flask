# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from passlib.hash import pbkdf2_sha256

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Boolean(), default=1, nullable=False)

    def __repr__(self):
        return '%s - %s' % (self.id, self.username)

    def get_user_by_email(self):
        try:
            return User.query.filter(User.email==self.email).first()
        except Exception as e:
            print("Erro ao listar o usuário.")
            return []

    def get_user_by_id(self):
        try:
            return User.query.filter(User.id==self.id).first()
        except Exception as e:
            print("Erro ao listar o usuário.")
            return []

    def get_users(self):
        try:
            return User.query.all()
        except Exception as e:
            print("Erro ao listar usuários.")
            return []  

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def update(self, obj):
        try:
            res = db.session.query(User).filter(User.id == self.id).update(obj)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def delete(self):
        try:
            User.query.filter(User.id==self.id).delete()
            return True
        except Exception as e:
            return False

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def hash_password(self, password):
        try:
            return self.pbkdf2_sha256.hash(password)
        except Exception as e:
            print("Erro ao criptografar senha %s" % e)

    def verify_password(self, password, password_database):
        try:
            return pbkdf2_sha256.verify(password, password_database)
        except ValueError:
            return False