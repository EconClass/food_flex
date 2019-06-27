from django.conf.urls import url, include
from rest_framework import routers
from api.views import RestaurantViewSet

router = routers.DefaultRouter()

# router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'auth/', include('rest_framework.urls'))
]
