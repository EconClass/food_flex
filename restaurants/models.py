from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    url = models.URLField(max_length=10000)
    state = models.CharField(max_length=60)
    image_url =  models.URLField(max_length=10000)

    def __str__(self):
        return self.name
