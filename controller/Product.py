from datetime import datetime

from model.Product import Product

class ProductController():
    def __init__(self):
        self.product_model = Product()

    def get_products(self, limit):    
        result = []
        try:
            res = self.product_model.get_all(limit=limit)

            for r in res:
                result.append({
                    'id': r.id,
                    'name': r.name,
                    'description': r.description,
                    'qtd': str(r.qtd),
                    'price': str(r.price),
                    'image': r.image,
                    'date_created': r.date_created
                })
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }
        
    def get_product_by_id(self, product_id):    
        result = {}
        try:
            self.product_model.id = product_id
            res = self.product_model.get_product_by_id()
            
            result = {
                'id': res.id,
                'name': res.name,
                'description': res.description,
                'qtd': str(res.qtd),
                'price': str(res.price),
                'image': res.image,
                'date_created': res.date_created
            }

            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }