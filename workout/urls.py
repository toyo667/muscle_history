from django.urls import include, path
from rest_framework import routers

from workout.views.master import ConditionListViewSets, TrainingAreaListViewSet, WorkoutFeelingListViewSets

from .views.training import WorkoutItemViewSet, WorkoutSessionViewSet, WorkoutViewSet

v1_router = routers.SimpleRouter()
v1_router.register(r"workout-item", WorkoutItemViewSet, basename="workout-item")
v1_router.register(r"workout-session", WorkoutSessionViewSet, basename="workout-session")
v1_router.register(r"workout", WorkoutViewSet, basename="workout")

# マスタデータ
v1_router.register(r"training-area", TrainingAreaListViewSet, basename="training-area")
v1_router.register(r"workout-feeling", WorkoutFeelingListViewSets, basename="workout-feeling")
v1_router.register(r"condition", ConditionListViewSets, basename="condition")

urlpatterns = [path("", include(v1_router.urls))]
