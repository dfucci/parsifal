# coding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings

from parsifal.reviews.models import Review, Source
from parsifal.reviews.conducting.utils import BibitexSanitizer


class ImportBibitexTest(TestCase):

    def setUp(self):
        path = settings.PROJECT_DIR.child('reviews').child('conducting').child('tests').child('data').child('single_entry.bib')
        with open(path) as f:
            self.bibtex_file = f
            self.new_bibtex_file = BibitexSanitizer(self.bibtex_file).sanitize()

    def test_file_is_correctly_loadded(self):
        self.assertIsNotNone(self.bibtex_file)

    def test_file_contains_text(self):
        self.assertRegexpMatches(self.new_bibtex_file, r'Jansen20141508')

    def test_curly_braces(self):
        self.assertRegexpMatches(self.new_bibtex_file, r'volume={"56"},')

    def test_multiple_import_keywords(self):
        actual = r'keywords={Software ecosystem health; Open source ecosystems; Software repository mining},'
        self.assertRegexpMatches(self.new_bibtex_file, actual)

    def test_only_one_keywords_line(self):
        actual = self.new_bibtex_file.count('keywords=')
        self.assertEquals(actual, 1)

