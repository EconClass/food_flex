from django.db import models
from restaurants.models import Restaurant
from django.contrib.auth.models import User

class Account(User):
    vistedRestaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.username
 