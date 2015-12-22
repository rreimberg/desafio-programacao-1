# -*- coding: utf-8 -*-

import os

from flask import (Blueprint, current_app, request, render_template,
                   redirect, url_for)
from werkzeug import secure_filename

from desafio.business.purchase import Purchase

site = Blueprint('site', __name__)


@site.route("/")
def index():
    return redirect(url_for('site.upload_form'))


@site.route("/upload", methods=['GET'])
def upload_form():
    return render_template('upload_form.html')


@site.route("/upload", methods=["POST"])
def post_customer_file():
    _file = request.files['file']

    if _file:
        filename = secure_filename(_file.filename)
        _file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('site.check_uploaded_file',
                                filename=filename))


@site.route('/uploaded/<filename>', methods=["GET"])
def check_uploaded_file(filename):

    purchase = Purchase.process_from_uploaded_file(filename)

    return render_template('check_uploaded_file.html',
                           purchase=purchase, filename=filename)


@site.route("/save_purchase", methods=["POST"])
def post_save_purchase():

    filename = request.form['filename']

    purchase = Purchase.process_from_uploaded_file(filename)
    purchase.save()

    return redirect(url_for('site.show_purchase', filename=filename))


@site.route('/uploaded/<filename>', methods=["GET"])
def show_purchase(filename):
    pass
