from datetime import datetime

from model.Product import Product

class ProductController():
    def __init__(self):
        self.product_model = Product()

    def save_product(self, obj):
        self.product_model.name = obj['name']
        self.product_model.description = obj['description']
        self.product_model.qtd = obj['qtd']
        self.product_model.price = obj['price']
        self.product_model.date_created = datetime.now()
        self.product_model.status = 1
        self.product_model.category = obj['category']
        self.product_model.user_created = obj['user_created']
        return self.product_model.save()

    def update_product(self, obj):
        self.product_model.id = obj['id']
        return self.product_model.update(obj)

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
        return {
            'result': result,
            'status': status
        }