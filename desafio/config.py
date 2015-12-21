# -*- coding: utf-8 -*-

import os


class Configuration(object):

    ALLOWED_EXTENSIONS = set(['tab'])

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/desafio.db'.format(
        os.path.abspath(os.path.dirname(__file__))
    )

    UPLOAD_FOLDER = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'static', 'uploads'))

    DEBUG = True
