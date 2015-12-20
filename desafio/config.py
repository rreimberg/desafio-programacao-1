# -*- coding: utf-8 -*-

import os


class Configuration(object):

    ALLOWED_EXTENSIONS = set(['tab'])

    UPLOAD_FOLDER = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'static', 'uploads'))

    DEBUG = True
