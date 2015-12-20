

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

    def save(self):
        pass


class PurchaseItem(object):

    def __init__(self, *args):
        (self.purchaser_name, self.item_description, self.item_price,
         self.purchase_count, self.merchant_address, self.merchant_name) = args

    def __iter__(self):
        yield self.purchaser_name
        yield self.item_description
        yield self.item_price
        yield self.purchase_count
        yield self.merchant_address
        yield self.merchant_name

    def total(self):
        return self.item_price * self.purchase_count
