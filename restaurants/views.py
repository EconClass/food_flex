from django.views.generic import ListView
# from rest_framework.views import APIView
from .models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "home.html"
    # def get(self, )
        