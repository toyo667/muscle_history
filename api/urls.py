from django.urls import include, path
from rest_framework import routers

from .views.training import WorkoutItemViewSet

v1_router = routers.SimpleRouter()
v1_router.register(r"workout-item", WorkoutItemViewSet, basename="workout-titem")

urlpatterns = [path("v1/", include(v1_router.urls))]
