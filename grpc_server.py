# -*- coding: utf-8 -*-
import os
from concurrent import futures

import grpc

from app import create_app
from config import app_active
from model.Product import Product
from controller.User import UserController
from protos import produto_pb2, produto_pb2_grpc

GRPC_PORT = os.getenv('GRPC_PORT', '50051')

app = create_app(app_active)

class ProdutoService(produto_pb2_grpc.ProdutoServiceServicer):
    def GetProduto(self, request, context):
        # O token chega nos metadados da chamada, o equivalente aos headers do HTTP
        metadata = dict(context.invocation_metadata())
        access_token = metadata.get('access-token')
        if access_token is None:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Você precisa enviar um token de acesso')

        result = UserController().verify_auth_token(access_token)
        if result['status'] != 200:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, result['message'])

        with app.app_context():
            product = Product()
            product.id = request.id
            res = product.get_product_by_id()

            if res is None:
                context.abort(grpc.StatusCode.NOT_FOUND, 'Produto %s não encontrado no livro_flask' % request.id)

            return produto_pb2.ProdutoResponse(
                id=res.id,
                name=res.name,
                description=res.description,
                qtd=res.qtd,
                price=str(res.price)
            )

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produto_pb2_grpc.add_ProdutoServiceServicer_to_server(ProdutoService(), server)
    server.add_insecure_port('[::]:%s' % GRPC_PORT)
    server.start()

    print('Servidor gRPC aguardando requisições na porta %s...' % GRPC_PORT)
    server.wait_for_termination()

if __name__ == '__main__':
    main()
