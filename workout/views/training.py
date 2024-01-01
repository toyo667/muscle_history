from rest_framework import viewsets
from workout.models.training import Workout, WorkoutItem, WorkoutSession

from workout.serializers.training import (
    RecentWorkoutParamSerializer,
    WorkoutItemSerializer,
    WorkoutSerializer,
    WorkoutSessionSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.db.models import Q
import django_filters.rest_framework


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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["session"]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user).select_related("training_item", "session")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(parameters=[RecentWorkoutParamSerializer], responses={200: WorkoutSerializer(many=True), 204: {}})
    @extend_schema(description="指定したワークアウト種目の直近の結果を取得する。セッションIDは除外用", methods=["GET"])
    @action(detail=False, methods=["get"])
    def recent_workout(self, request):
        req_serializer = RecentWorkoutParamSerializer(data=request.query_params)
        req_serializer.is_valid(raise_exception=True)
        training_item = req_serializer.validated_data.get("training_item")  # type: ignore
        session = req_serializer.validated_data.get("session")  # type: ignore
        exclude = Q(session=session) if session else Q()
        recent_workout = self.get_queryset().order_by("-trained_at").filter(training_item=training_item).exclude(exclude).first()
        if not recent_workout:
            return Response({}, status.HTTP_204_NO_CONTENT)

        # 同じセッションの同じ種目のワークアウトをすべて取得
        samesession_workouts = self.get_queryset().filter(session=recent_workout.session, training_item=training_item)
        response_datas = []
        for workout in samesession_workouts:
            response_datas.append(self.get_serializer(workout).data)
        return Response(response_datas, status.HTTP_200_OK)
