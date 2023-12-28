from rest_framework import serializers

from api.models.training import WorkoutItem


class WorkoutItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutItem
        fields = ["id", "training_name", "category"]
