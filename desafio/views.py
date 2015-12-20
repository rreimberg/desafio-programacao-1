# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, url_for

site = Blueprint('site', __name__)


@site.route("/")
def index():
    return redirect(url_for('site.upload_form'))


@site.route("/upload", methods=['GET'])
def upload_form():
    return render_template('upload_form.html')
