# -*- coding: utf-8 -*-
import os
import json
from kafka import KafkaConsumer

from app import create_app
from config import app_active
from model.EventoPedido import EventoPedido

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC_PEDIDOS = 'pedidos'

app = create_app(app_active)

def main():
    consumer = KafkaConsumer(
        TOPIC_PEDIDOS,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id='livro-flask-analytics',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    print('Aguardando eventos de pedidos no tópico "%s"...' % TOPIC_PEDIDOS)

    for message in consumer:
        data = message.value
        print('Evento recebido:', data)

        with app.app_context():
            evento = EventoPedido()
            evento.pedido_id = data['pedido_id']
            evento.product_id = data['product_id']
            evento.product_name = data.get('product_name')
            evento.qtd = data['qtd']
            evento.preco_total = data.get('preco_total')
            evento.save()

if __name__ == '__main__':
    main()
