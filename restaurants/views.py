from django.views.generic import ListView
from django.shortcuts import render
from .utils import call_yelp_api
from .models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "home.html"


class SearchListView(ListView):
    model = Restaurant
    template_name = "search.html"
    def get(self, request):
        context = call_yelp_api()
        return render(request, self.template_name, context)
