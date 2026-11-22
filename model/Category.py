# -*- coding: utf-8 -*-
from sqlalchemy import func

from extensions import db
from model.User import User

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