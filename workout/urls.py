from django.urls import include, path
from rest_framework import routers

from .views.training import WorkoutItemViewSet, WorkoutSessionViewSet, WorkoutViewSet

v1_router = routers.SimpleRouter()
v1_router.register(r"workout-item", WorkoutItemViewSet, basename="workout-item")
v1_router.register(r"workout-session", WorkoutSessionViewSet, basename="workout-session")
v1_router.register(r"workout", WorkoutViewSet, basename="workout")

urlpatterns = [path("", include(v1_router.urls))]
