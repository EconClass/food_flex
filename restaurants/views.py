from django.views.generic import ListView
from .utils import *
from .models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "home.html"
    