# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_uris(app):
    from desafio.views import site
    app.register_blueprint(site)


def create_app():
    app = Flask(__name__)
    app.config.from_object('desafio.config.Configuration')

    db.init_app(app)
    app.db = db

    register_uris(app)

    return app
