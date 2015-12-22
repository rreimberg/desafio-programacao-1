

from desafio import db
from desafio.models import Merchant, Product, Customer, Purchase as PurchaseModel
from desafio.parser import parse_uploaded_file


class Purchase(object):

    items = []

    @classmethod
    def process_from_uploaded_file(cls, filename):
        data = parse_uploaded_file(filename)

        obj = cls()

        for item in data[1:]:
            obj.items.append(PurchaseItem(*item))

        return obj

    @property
    def total(self):
        _total = 0
        for item in self.items:
            _total += item.total()

        return _total

    def save(self):
        for item in self.items:
            merchant = Merchant.get_or_create(name=item.merchant_name, address=item.merchant_address)
            product = Product.get_or_create(merchant=merchant, description=item.item_description, price=item.item_price)
            customer = Customer.get_or_create(name=item.purchaser_name)

            purchase = PurchaseModel(customer=customer, product=product, item_count=item.purchase_count)

            db.session.add(merchant)
            db.session.add(product)
            db.session.add(customer)
            db.session.add(purchase)
            db.session.commit()


class PurchaseItem(object):

    def __init__(self, purchaser_name, item_description, item_price,
                 purchase_count, merchant_address, merchant_name):
        self.purchaser_name = purchaser_name
        self.item_description = item_description
        self.item_price = float(item_price)
        self.purchase_count = int(purchase_count)
        self.merchant_address = merchant_address
        self.merchant_name = merchant_name

    def __iter__(self):
        yield self.purchaser_name
        yield self.item_description
        yield self.item_price
        yield self.purchase_count
        yield self.merchant_address
        yield self.merchant_name

    def total(self):
        return self.item_price * self.purchase_count
