from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views
from .models import Restaurant

class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(
            name = 'Four Barrel Coffee',
            address = '375 Valencia St',
            city = 'San Francisco',
            url = 'https://www.yelp.com/biz/four-barrel-coffee-san-francisco',
            state = 'CA'
        )

        Restaurant.objects.create(
            name = 'Saigon Sandwich',
            address = '560 Larkin Street',
            city = 'San Francisco',
            url = 'https://www.yelp.com/biz/saigon-sandwich-san-francisco',
            state = 'CA'
        )

    def test_correct_restaurant_info(self):
        coffe = Restaurant.objects.get(name='Four Barrel Coffee')
        sandwich = Restaurant.objects.get(name='Saigon Sandwich')
        

class RestaurantViewTestCase(TestCase):

    def test_restaurats_view(self):
        res = self.client.get(reverse('restaurants'))
        self.assertEquals(res.status_code, 200)


    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('restaurants'))
        self.assertTemplateUsed(res, 'restaurant.html')