from loja import db

from datetime import datetime

'''
class Addprodutos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    minimun = db.Column(db.Float(10), nullable=False)
    amount_per_package = db.Column(db.Float, nullable=False)
    max_availability = db.Column(db.Float, nullable=False)
    
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    
    def __repr__(self):
        return '<Addprodutos %r>' % self.name
''' 


class Produtos(db.Model):
    __tablename__ = 'produto'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    minimun = db.Column(db.Float)
    amount_per_package = db.Column(db.Float)
    max_availability = db.Column(db.Float)

    def __init__(self, name, price, minimun, amount_per_package, max_availability):
        self.name = name
        self.price = price
        self.minimun = minimun
        self.amount_per_package = amount_per_package
        self.max_availability = max_availability

    db.create_all()