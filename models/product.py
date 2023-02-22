from main import db

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    price=db.Column(db.Float)
    amount=db.Column(db.Integer)

    def __init__(self,name,price,amount):
        self.name=name
        self.price=price
        self.amount=amount