# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.User import User
from model.Category import Category
from model.Product import Product

from admin.Views import UserView

def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', template_mode='bootstrap3')

    admin.add_view(UserView(User, db.session, "Usuários"))
    admin.add_view(ModelView(Category, db.session, 'Categorias', category="Produtos"))
    admin.add_view(ModelView(Product, db.session, "Produtos", category="Produtos"))