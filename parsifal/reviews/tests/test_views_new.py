# coding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User


class NewReview(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='john', password='123', email='joh@doe.com')
        self.client.login(username='john', password='123')
        self.response = self.client.get('/reviews/new/')

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
         self.assertTemplateUsed(self.response, 'reviews/new.html')

