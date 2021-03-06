# -*- coding: utf-8 -*-

from desafio import db


class BaseModel(db.Model):

    __abstract__ = True

    @classmethod
    def get_or_create(cls, *args, **kwargs):
        element = cls.query.filter_by(**kwargs).first()
        if not element:
            element = cls(**kwargs)

        return element


class File(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def total_purchases_value(self):
        _total = 0
        for purchase in self.purchases:
            _total += purchase.total()

        return _total


class Merchant(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.Text)


class Product(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    id_merchant = db.Column(db.Integer, db.ForeignKey('merchant.id'))
    description = db.Column(db.String(80))
    price = db.Column(db.Float)

    merchant = db.relationship('Merchant', backref=db.backref('products'))


class Customer(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


class Purchase(BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    id_file = db.Column(db.Integer, db.ForeignKey('file.id'))
    id_customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    item_count = db.Column(db.Integer)

    customer = db.relationship('Customer', backref=db.backref('purchases'))
    product = db.relationship('Product', backref=db.backref('purchases'))
    file = db.relationship('File', backref=db.backref('purchases'))

    def total(self):
        return self.item_count * self.product.price
