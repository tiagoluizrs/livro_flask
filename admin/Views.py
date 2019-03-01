# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    can_view_details = True
    
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email']
    column_editable_list = ['username', 'email']
    column_exclude_list = ['password']

    create_modal = True
    edit_modal = True

    can_export = True

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    def on_model_change(self, form, User, is_created):
        if form.password.data is not None:
            User.set_password(form.password.data)
        else:
           del form.password