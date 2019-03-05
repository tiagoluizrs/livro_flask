# -*- coding: utf-8 -*-
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return self.name

    def get_total_categories(self):
        try:
            res = db.session.query(func.count(Category.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res