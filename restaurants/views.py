from django.views.generic import ListView
from django.shortcuts import render
from .utils import call_api_with_location
from .models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "home.html"


class SearchListView(ListView):
    model = Restaurant
    template_name = "home.html"
    # def get(self, request):
    #     context = call_api_with_location()
    #     return context
