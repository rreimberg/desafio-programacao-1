# -*- coding: utf-8 -*-

import mock

from .base import BaseTestCase

from desafio import db
from desafio.business import DuplicatedFilename, save_uploaded_file, save_purchase
from desafio.models import Customer, File, Merchant, Product, Purchase


class TestRequestFile(object):

            filename = 'test_filename'
            save = mock.Mock()


class DBSaveTestCase(BaseTestCase):

    def test_save_uploaded_file_with_duplicated_filename(self):

        _file = File(name='test_filename')
        db.session.add(_file)
        uploaded_file = TestRequestFile()

        with self.assertRaises(DuplicatedFilename):
            save_uploaded_file(uploaded_file)

    def test_save_uploaded_file_success(self):

        _file = TestRequestFile()

        self.app.config['UPLOAD_FOLDER'] = '/tmp'

        f = save_uploaded_file(_file)

        self.assertEqual('test_filename', f)
        _file.save.assert_called_once_with('/tmp/test_filename')

    @mock.patch('desafio.business.parse_uploaded_file')
    def test_save_purchase_success(self, parser_mock):

        parser_mock.return_value = [
            ['purchaser name', 'item description', 'item price', 'purchase count', 'merchant address', 'merchant name'],
            ['Zezinho', 'R$10 off', '10.0', '2', 'local', 'pizza'],
            ['Luluzinha', 'R$20 off', '20.0', '3', 'local', 'pizza'],
        ]

        save_purchase('test_filename')

        self.assertEqual(1, File.query.count())
        self.assertEqual(2, Customer.query.count())
        self.assertEqual(2, Product.query.count())
        self.assertEqual(1, Merchant.query.count())
        self.assertEqual(2, Purchase.query.count())
