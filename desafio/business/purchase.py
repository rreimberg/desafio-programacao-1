

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
        pass


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
