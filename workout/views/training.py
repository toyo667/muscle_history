from rest_framework import viewsets
from workout.models.training import Workout, WorkoutItem, WorkoutSession

from workout.serializers.training import WorkoutItemSerializer, WorkoutSerializer, WorkoutSessionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response


@extend_schema(tags=["workout-item"])
class WorkoutItemViewSet(viewsets.ModelViewSet):
    """トレーニング種目"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutItemSerializer
    queryset = WorkoutItem.objects.none()

    def get_queryset(self):
        return WorkoutItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["workout-session"])
class WorkoutSessionViewSet(viewsets.ModelViewSet):
    """ワークアウトセッション(1回のトレーニング)"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.none()

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(responses={200: WorkoutSessionSerializer, 204: {}})
    @extend_schema(description="現在アクティブになっているワークアウトセッションを取得する。", methods=["GET"])
    @action(detail=False, methods=["get"])
    def active(self, request):
        wo_sessions = self._get_active_session()
        if wo_sessions:
            serializer = self.get_serializer(wo_sessions)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

    def _get_active_session(self) -> WorkoutSession | None:
        return self.get_queryset().filter(finished_at__isnull=True).order_by("-started_at").first()


@extend_schema(tags=["workout"])
class WorkoutViewSet(viewsets.ModelViewSet):
    """ワークアウト内容"""

    permission_classes = (IsAuthenticated,)

    serializer_class = WorkoutSerializer
    queryset = Workout.objects.none()

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
