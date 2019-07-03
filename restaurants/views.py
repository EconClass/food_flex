# from django.views.generic import ListView
from rest_framework.views import APIView
from .models import Restaurant


class RestaurantListView(APIView):
    model = Restaurant
    template_name = "restaurant.html"
    # def get(self, )
