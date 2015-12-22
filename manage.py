#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from desafio import create_app

app = create_app()

manager = Manager(app)


@manager.command
def create_db():
    from desafio import db
    db.create_all()


if __name__ == "__main__":
    manager.run()
