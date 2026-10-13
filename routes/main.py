# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, render_template
from flask_login import login_user, logout_user

from controller.User import UserController

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Meu primeiro run'

@main_bp.route('/login/')
def login():
    return render_template('login.html', data={'status': 200, 'msg': None, 'type': None})

@main_bp.route('/login/', methods=['POST'])
def login_post():
    user = UserController()

    email = request.form['email']
    password = request.form['password']

    result = user.login(email, password)

    if result:
        if result.role == 4:
            return render_template('login.html', data={'status': 401, 'msg': 'Seu usuário não tem permissão para acessar o admin', 'type':2})
        else:
            login_user(result)
            return redirect('/admin')
    else:
        return render_template('login.html', data={'status': 401, 'msg': 'Dados de usuário incorretos', 'type': 1})

@main_bp.route('/recovery-password/')
def recovery_password():
    return render_template('recovery.html', data={'status': 200, 'msg': None, 'type': None})

@main_bp.route('/recovery-password/', methods=['POST'])
def send_recovery_password():
    user = UserController()

    result = user.recovery(request.form['email'])

    if result['status_code'] == 200:
        return render_template('recovery.html', data={'status': result['status_code'], 'msg': 'Você receberá um e-mail em sua caixa para alteração de senha.', 'type': 3})
    else:
        return render_template('recovery.html', data={'status': result['status_code'], 'msg': result['body'], 'type': 1})

@main_bp.route('/new-password/<recovery_code>')
def new_password(recovery_code):
    user = UserController()
    result = user.verify_auth_token(recovery_code)

    if result['status'] == 200:
        res = user.get_user_by_recovery(str(recovery_code))
        if res is not None:
            return render_template('new_password.html', data={'status': result['status'], 'msg': None, 'type': None, 'recovery_code': recovery_code})
        else:
            return render_template('recovery.html', data={'status': 400, 'msg': 'Erro ao tentar acessar os dados do usuário. Tente novamente mais tarde.', 'type': 1})
    else:
        return render_template('recovery.html', data={'status': result['status'], 'msg': 'Token expirado ou inválido, solicite novamente a alteração de senha', 'type': 1})

@main_bp.route('/new-password/', methods=['POST'])
def send_new_password():
    user = UserController()
    recovery_code = request.form['recovery_code']
    password = request.form['password']

    result = user.verify_auth_token(recovery_code)
    res = user.get_user_by_recovery(recovery_code) if result['status'] == 200 else None

    if res is None:
        return render_template('recovery.html', data={'status': 400, 'msg': 'Token expirado ou inválido, solicite novamente a alteração de senha', 'type': 1})

    if user.new_password(res.id, password):
        return render_template('login.html', data={'status': 200, 'msg': 'Senha alterada com sucesso!', 'type': 3})
    else:
        return render_template('new_password.html', data={'status': 401, 'msg': 'Erro ao alterar senha.', 'type': 1, 'recovery_code': recovery_code})

@main_bp.route('/logout')
def logout_send():
    logout_user()
    return render_template('login.html', data={'status': 200, 'msg': 'Usuário deslogado com sucesso!', 'type':3})
