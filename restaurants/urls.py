from django.urls import path
from django.views.generic import TemplateView
from .views import RestaurantListView

urlpatterns = [
    path('', RestaurantListView.as_view()),
]

