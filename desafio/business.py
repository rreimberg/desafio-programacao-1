# -*- coding: utf-8 -*-

import os
import unicodecsv

from flask import current_app
from werkzeug import secure_filename

from desafio import db
from desafio.models import (Customer, File, Merchant, Product, Purchase)


class DuplicatedFilename(Exception):
    pass


def parse_uploaded_file(filename):
    _file = '{0}/{1}'.format(current_app.config['UPLOAD_FOLDER'], filename)

    data = []
    reader = unicodecsv.reader(open(_file, 'rb'),
                               delimiter='\t', lineterminator='\n')

    for line in reader:
        data.append(line)

    return data


def save_uploaded_file(uploaded_file):
    filename = secure_filename(uploaded_file.filename)

    if File.query.filter_by(name=filename).count():
        raise DuplicatedFilename

    uploaded_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return filename


def save_purchase(filename):

    _file = File(name=filename)
    db.session.add(_file)

    data = parse_uploaded_file(filename)

    for item in data[1:]:

        (purchaser_name, item_description, item_price,
            purchase_count, merchant_address, merchant_name) = item

        customer = Customer.get_or_create(name=purchaser_name)

        merchant = Merchant.get_or_create(
            name=merchant_name,
            address=merchant_address)

        product = Product.get_or_create(
            merchant=merchant,
            description=item_description,
            price=item_price)

        purchase = Purchase(
            file=_file,
            customer=customer,
            product=product,
            item_count=purchase_count)

        db.session.add(merchant)
        db.session.add(product)
        db.session.add(customer)
        db.session.add(purchase)
        db.session.commit()
