# -*- coding: utf-8 -*-
from flask import Blueprint, request, Response, json

from controller.User import UserController
from controller.Product import ProductController
from routes.decorators import auth_token_required

api_bp = Blueprint('api', __name__)

@api_bp.route('/products/', methods=['GET'])
@api_bp.route('/products/<limit>', methods=['GET'])
@auth_token_required
def get_products(limit=None):
    header = {
        'access_token': request.headers['access_token'],
        "token_type": "JWT"
    }

    product = ProductController()
    response = product.get_products(limit=limit)
    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

@api_bp.route('/product/<product_id>', methods=['GET'])
@auth_token_required
def get_product(product_id):
    header = {
        'access_token': request.headers['access_token'],
        "token_type": "JWT"
    }

    product = ProductController()
    response = product.get_product_by_id(product_id = product_id)

    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

@api_bp.route('/user/<user_id>', methods=['GET'])
@auth_token_required
def get_user_profile(user_id):
    header = {
        'access_token': request.headers['access_token'],
        "token_type": "JWT"
    }

    user = UserController()
    response = user.get_user_by_id(user_id=user_id)

    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

@api_bp.route('/login_api/', methods=['POST'])
def login_api():
    header = {}
    user = UserController()

    email = request.json['email']
    password = request.json['password']

    result = user.login(email, password)
    code = 401
    response = {"message": "Usuário não autorizado", "result": []}

    if result:
        if result.active:
            result = {
                'id': result.id,
                'username': result.username,
                'email': result.email,
                'date_created': result.date_created,
                'active': result.active
            }

            header = {
                "access_token": user.generate_auth_token(result),
                "token_type": "JWT"
            }
            code = 200
            response["message"] = "Login realizado com sucesso"
            response["result"] = result

    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), code, header
