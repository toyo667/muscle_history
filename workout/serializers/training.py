from dataclasses import field
from pkg_resources import require
from rest_framework import serializers

from workout.models.training import Workout, WorkoutItem, WorkoutSession


class WorkoutItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutItem
        fields = ["id", "training_name", "category"]


class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ["id", "started_at", "finished_at", "condition"]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "training_item", "feeling", "session", "rep_count", "set_count", "weight_kg", "trained_at"]


class RecentWorkoutParamSerializer(serializers.Serializer):
    training_item = serializers.UUIDField()
    session = serializers.UUIDField(required=False)
