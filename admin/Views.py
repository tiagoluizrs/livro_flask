# -*- coding: utf-8 -*-
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from config import app_config, app_active

from model.User import User
from model.Category import Category
from model.Product import Product

config = app_config[app_active]

class HomeView(AdminIndexView):
    extra_css = [config.URL_MAIN + 'static/css/home.css','https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']

    @expose('/')
    def index(self):
        user_model = User()
        category_model = Category()
        product_model = Product()

        users = user_model.get_total_users()
        categories = category_model.get_total_categories()
        products = product_model.get_total_products()
        last_products = product_model.get_last_products()

        return self.render('home_admin.html', report={
            'users': users[0],
            'categories': categories[0],
            'products': products[0]
        }, last_products=last_products)

class UserView(ModelView):
    column_labels = {
        'funcao': 'Função',
        'username': 'Nome de usuário',
        'email': 'E-mail',
        'date_created': 'Data de Criação',
        'last_update': 'Última atualização',        
        'status': 'Estado',
        'password': 'Senha',
    }

    column_descriptions = {
        'funcao': 'Função no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de Criação do usuário no sistema',
        'last_update': 'Última atualização desse usuário no sistema',        
        'status': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema',
    }

    column_exclude_list = ['password']
    form_excluded_columns = ['last_update']

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'funcao']
    column_editable_list = ['username', 'email', 'funcao', 'status']
    create_modal = True
    edit_modal = True
    can_export = True
    column_sortable_list = ['username']
    column_default_sort = [('username', True), ('date_created', True)]
    column_details_exclude_list = ['password', 'recovery_code']
    column_export_exclude_list = ['password', 'recovery_code']

    export_types = ['json', 'yaml', 'csv', 'xls', 'df']

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password