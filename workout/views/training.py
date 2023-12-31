from rest_framework import viewsets
from workout.models.training import Workout, WorkoutItem, WorkoutSession

from workout.serializers.training import WorkoutItemSerializer, WorkoutSerializer, WorkoutSessionSerializer
from rest_framework.permissions import IsAuthenticated


class WorkoutItemViewSet(viewsets.ModelViewSet):
    """トレーニング種目"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutItemSerializer
    queryset = WorkoutItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    """ワークアウトセッション(1回のトレーニング)"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutViewSet(viewsets.ModelViewSet):
    """ワークアウト内容"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
