# -*- coding: utf-8 -*-

from flask import (Blueprint, request, render_template,
                   redirect, url_for)

from desafio.business import save_purchase, save_uploaded_file
from desafio.models import File

site = Blueprint('site', __name__)


@site.route("/")
def index():
    return redirect(url_for('site.start_page'))


@site.route("/start")
def start_page():
    files = File.query.all()
    return render_template('start.html', files=files)


@site.route("/upload", methods=['GET'])
def upload_form():
    return render_template('upload_form.html')


@site.route("/upload", methods=["POST"])
def post_customer_file():
    uploaded_file = request.files['file']

    if uploaded_file:
        filename = save_uploaded_file(uploaded_file)

        save_purchase(filename)

        return redirect(url_for('site.show_purchase',
                                filename=filename))


@site.route("/save_purchase", methods=["POST"])
def post_save_purchase():

    filename = request.form['filename']
    save_purchase(filename)

    return redirect(url_for('site.show_purchase', filename=filename))


@site.route('/show/<filename>', methods=["GET"])
def show_purchase(filename):
    uploaded_file = File.query.filter_by(name=filename).first()

    return render_template('show_purchase.html', uploaded_file=uploaded_file)
