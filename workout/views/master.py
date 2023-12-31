from rest_framework import mixins, viewsets, serializers

from workout.models.master import TrainingArea, WorkoutFeeling, Condition
from drf_spectacular.utils import extend_schema


class TrainingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingArea
        fields = ("id", "training_area", "order")


class WorkoutFeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutFeeling
        fields = ("id", "feel", "order")


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ("id", "feel", "order")


@extend_schema(tags=["master"])
class TrainingAreaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TrainingArea.objects.all()
    serializer_class = TrainingAreaSerializer


@extend_schema(tags=["master"])
class WorkoutFeelingListViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WorkoutFeeling.objects.all()
    serializer_class = WorkoutFeelingSerializer


@extend_schema(tags=["master"])
class ConditionListViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
