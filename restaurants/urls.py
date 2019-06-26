from django.urls import path
from . import views

urlpatterns = [
    # path(),
    path('restaurants/', views.RestaurantListView.as_view()),
]