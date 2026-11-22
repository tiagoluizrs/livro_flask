# -*- coding: utf-8 -*-
from functools import wraps

from flask import request, abort

from controller.User import UserController

def auth_token_required(f):
    @wraps(f)
    def verify_token(*args, **kwargs):
        user = UserController()
        try:
            result = user.verify_auth_token(request.headers['access_token'])
            if result['status'] == 200:
                return f(*args, **kwargs)
            else:
                abort(result['status'], result['message'])
        except KeyError as e:
            abort(401, 'Você precisa enviar um token de acesso')

    return verify_token
