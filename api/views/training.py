from rest_framework import viewsets
from api.models.training import Workout, WorkoutItem, WorkoutSession

from api.serializers.training import WorkoutItemSerializer, WorkoutSerializer, WorkoutSessionSerializer


class WorkoutItemViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutItemSerializer
    queryset = WorkoutItem.objects.all()


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.all()


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()
