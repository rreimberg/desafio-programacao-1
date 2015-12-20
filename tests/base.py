# -*- coding: utf-8 -*-

import os

from unittest import TestCase

from desafio.app import create_app


class BaseTestCase(TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.app = self.create_app()
        self.fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

        self.context = self.app.app_context()
        self.context.push()

    def create_app(self):
        app = create_app()
        return app

    def tearDown(self):
        self.context.pop()
        super(BaseTestCase, self).tearDown()
