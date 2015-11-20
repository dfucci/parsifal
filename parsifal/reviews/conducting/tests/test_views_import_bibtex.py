# coding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings

from parsifal.reviews.models import Review, Source
from parsifal.reviews.conducting.utils import fix_bibtex_file


class ImportBibitexTest(TestCase):

    def setUp(self):
        path = settings.PROJECT_DIR.child('reviews').child('conducting').child('tests').child('data').child('science.bib')
        with open(path) as f:
            self.bibtex_file = f.readlines()
        self.new_bibtex_file = fix_bibtex_file(self.bibtex_file)

    def test_file_is_correctly_loadded(self):
        self.assertTrue(len(self.bibtex_file), 0)

    def test_file_contains_text(self):
        self.assertRegexpMatches(self.bibtex_file[0], r'Jansen20141508')

    def test_if_bibtex_file_is_list(self):
        self.assertEquals(type(self.bibtex_file), list)

    def test_curly_braces(self):
        self.assertEquals(self.new_bibtex_file[0][3], 'volume={"56"},')

    def test_multiple_import_keywords(self):
        self.assertEquals(self.new_bibtex_file[0][13], 'keywords={"Software ecosystems health; Open source ecosystems; Software repository mining"},')
        self.assertFalse("keyword" in self.new_bibtex_file[13])

    def test_new_bibtex_file_length(self):
        self.assertEquals(len(self.new_bibtex_file), 3)
