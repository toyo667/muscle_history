from django.urls import include, path
from rest_framework import routers

from auth_api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
