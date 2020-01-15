from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Gibson



class GibsonTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='jb',
            email='seanmoore013@gmail.com',
            password='7942qwer'
        )

        self.gibson = Gibson.objects.create(
            title='SG Custom Shop Deluxe',
            body='Gibson Custom Shop is the pinnacle of craftsmanship, quality, and sound excellence. Each instrument celebrates Gibson`s legacy through accuracy, authenticity and attention to detail.' ,
            author=self.user,
        )

    def test_string_representation(self):
        gibson = Gibson(title='SG Custom Shop Deluxe')
        self.assertEqual(str(gibson), gibson.title)

    def test_gibson_content(self):
        self.assertEqual(f'{self.gibson.title}', 'SG Custom Shop Deluxe')
        self.assertEqual(f'{self.gibson.author}', 'jb')
        self.assertEqual(f'{self.gibson.body}', 'Gibson Custom Shop is the pinnacle of craftsmanship, quality, and sound excellence. Each instrument celebrates Gibson`s legacy through accuracy, authenticity and attention to detail.')

    def test_gibson_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_gibson_detail_view(self):
        response = self.client.get('/gibson/1/')
        no_response = self.client.get('/gibson/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'SG Custom Shop Deluxe')
        self.assertTemplateUsed(response, 'gibson_detail.html')