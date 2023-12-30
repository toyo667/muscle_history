from uuid import uuid4
from django.db import models
from api.models.master import TrainingArea, WorkoutFeeling, Condition


class WorkoutItem(models.Model):
    class Meta:
        verbose_name = "トレーニング種目"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    training_name = models.CharField(verbose_name="トレーニング種目", max_length=64)
    category = models.ForeignKey(TrainingArea, on_delete=models.CASCADE)


class WorkoutSession(models.Model):
    class Meta:
        verbose_name = "ワークアウトセッション"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    started_at = models.DateTimeField(verbose_name="トレーニング開始日時", auto_now_add=True)
    finished_at = models.DateTimeField(verbose_name="トレーニング終了日時", null=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)


class Workout(models.Model):
    class Meta:
        verbose_name = "ワークアウト"
        ordering = ["-trained_at"]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    training_item = models.ForeignKey(WorkoutItem, on_delete=models.CASCADE)
    feeling = models.ForeignKey(WorkoutFeeling, on_delete=models.CASCADE)
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)

    rep_count = models.IntegerField(verbose_name="レップ数")
    set_count = models.IntegerField(verbose_name="セット数")
    weight_kg = models.FloatField(verbose_name="重さ(kg)")

    trained_at = models.DateTimeField(verbose_name="トレーニング日時", auto_now_add=True)
