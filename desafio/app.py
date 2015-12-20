# -*- coding: utf-8 -*-

from flask import Flask


def register_uris(app):
    from desafio.views import site
    app.register_blueprint(site)


def create_app():
    app = Flask(__name__)
    app.config.from_object('desafio.config.Configuration')

    register_uris(app)

    return app
