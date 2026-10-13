# -*- coding: utf-8 -*-
import os
import json
import pika

from app import create_app
from config import app_active
from extensions import db
from model.Product import Product

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
QUEUE_PEDIDO_CRIADO = 'pedido_criado'

app = create_app(app_active)

def processar_pedido_criado(ch, method, properties, body):
    data = json.loads(body)
    print('Pedido recebido:', data)

    with app.app_context():
        product = Product()
        product.id = data['product_id']
        res = product.get_product_by_id()

        if res is not None:
            nova_qtd = max(res.qtd - data['qtd'], 0)
            db.session.query(Product).filter(Product.id == res.id).update({'qtd': nova_qtd})
            db.session.commit()
            print('Estoque atualizado. Produto %s agora tem %s unidades' % (res.id, nova_qtd))
        else:
            print('Produto %s não encontrado' % data['product_id'])

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    ))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_PEDIDO_CRIADO, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_PEDIDO_CRIADO, on_message_callback=processar_pedido_criado)

    print('Aguardando mensagens de pedidos criados...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
