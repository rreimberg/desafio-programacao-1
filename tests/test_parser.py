# -*- coding: utf-8 -*-

from .base import BaseTestCase

from desafio.parser import parse_uploaded_file


class ParserTestCase(BaseTestCase):

    def test_process_file_without_accents(self):

        self.app.config['UPLOAD_FOLDER'] = self.fixtures_path

        data = parse_uploaded_file('arquivo_sem_acentos.tab')

        expected = [
            ['nome', 'idade', 'sexo'],
            ['Ramon', '30', 'Masculino'],
            ['Rita', '14', 'Feminino'],
        ]

        self.assertEqual(data, expected)

    def test_process_file_with_accents(self):

        self.app.config['UPLOAD_FOLDER'] = self.fixtures_path

        data = parse_uploaded_file('arquivo_com_acentos.tab')

        expected = [
            ['nome', 'idade', 'sexo'],
            [u'João', '30', 'Masculino'],
            [u'Débora', '14', 'Feminino'],
        ]

        self.assertEqual(data, expected)
