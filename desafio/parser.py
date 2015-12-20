# -*- coding: utf-8 -*-

import unicodecsv

from flask import current_app


def parse_uploaded_file(filename):
    _file = '{0}/{1}'.format(current_app.config['UPLOAD_FOLDER'], filename)

    data = []
    reader = unicodecsv.reader(open(_file, 'rb'),
                               delimiter='\t', lineterminator='\n')

    for line in reader:
        data.append(line)

    return data
