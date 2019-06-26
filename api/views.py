from django.shortcuts import render
# from django.contrib.auth.models import User

from rest_framework import viewsets

from restaurants.models import Restaurant
from api.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
