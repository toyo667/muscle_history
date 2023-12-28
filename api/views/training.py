from rest_framework import viewsets
from api.models.training import WorkoutItem

from api.serializers.training import WorkoutItemSerializer


class WorkoutItemViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutItemSerializer
    queryset = WorkoutItem.objects.all()
