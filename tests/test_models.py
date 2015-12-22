# -*- coding: utf-8 -*-

from .base import BaseTestCase

from desafio import db
from desafio.models import File, Merchant, Product, Purchase


class ModelsTestCase(BaseTestCase):

    def test_get_or_create_with_simple_properties(self):

        merchant = Merchant(name='merchant 1', address='New Street')
        db.session.add(merchant)

        m1 = Merchant.get_or_create(name='merchant 1', address='New Street')

        self.assertEqual(merchant, m1)
        self.assertIsNotNone(m1.id)

        m2 = Merchant.get_or_create(name='merchant 2', address='New Street')
        self.assertIsNone(m2.id)

    def test_get_or_create_with_relationship(self):

        merchant = Merchant(name='merchant 1', address='New Street')
        db.session.add(merchant)

        product = Product(merchant=merchant, description='product 1', price=1.5)
        db.session.add(product)

        p1 = Product.get_or_create(description='product 1', price=1.5)

        self.assertEqual(product, p1)
        self.assertIsNotNone(p1.id)

        p2 = Product.get_or_create(description='product 2', price=2.9)
        self.assertIsNone(p2.id)

    def test_total_purchase_calculate(self):

        _file = File(name='test_filename')

        product1 = Product(description='product 1', price=1.5)
        product2 = Product(description='product 2', price=2)

        purchase1 = Purchase(file=_file, product=product1, item_count=5)
        purchase2 = Purchase(file=_file, product=product2, item_count=10)

        self.assertEqual(7.5, purchase1.total())

        self.assertEqual(27.5, _file.total_purchases_value())
