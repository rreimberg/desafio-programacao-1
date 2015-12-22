# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def set_config(app):
    app.config.from_object('desafio.config.base.Configuration')


def register_uris(app):
    from desafio.views import site
    app.register_blueprint(site)


def create_app(set_config=set_config):
    app = Flask(__name__)
    set_config(app)

    db.init_app(app)
    app.db = db

    register_uris(app)

    return app
