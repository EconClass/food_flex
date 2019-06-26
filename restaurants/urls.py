from django.urls import path
from .views import RestaurantListView

urlpatterns = [
    # path(),
    path('', RestaurantListView.as_view()),
]