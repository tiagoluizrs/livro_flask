# -*- coding: utf-8 -*-
from extensions import db

class EventoPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(60), nullable=True)
    qtd = db.Column(db.Integer, nullable=False)
    preco_total = db.Column(db.String(20), nullable=True)
    date_received = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return 'Evento do pedido %s' % self.pedido_id

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
