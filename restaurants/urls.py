from django.urls import path
# from django.views.generic import TemplateView
from .views import RestaurantListView, SearchListView

urlpatterns = [
    path('', RestaurantListView.as_view()),
    path('search/', SearchListView.as_view()),
]

