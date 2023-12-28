from cgi import print_arguments
from tabnanny import verbose
from uuid import uuid4
from django.db import models
from django.utils.translation import gettext as _


class TrainingArea(models.Model):
    class Meta:
        verbose_name = "トレーニング部位"
        ordering = ["id"]

    def __str__(self):
        return self.get_training_area_display()  # type: ignore

    TRAIN_ARM = "arm"
    TRAIN_BACK = "back"
    TRAIN_CHEST = "chest"
    TRAIN_LEG = "leg"
    TRAIN_ABDOMINAL = "abdominal"

    TRAINING_AREAS = (
        (TRAIN_ARM, _("腕")),
        (TRAIN_BACK, _("背中")),
        (TRAIN_CHEST, _("胸")),
        (TRAIN_LEG, _("脚")),
        (TRAIN_ABDOMINAL, _("腹")),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    training_area = models.CharField(verbose_name="トレーニング部位", max_length=64, choices=TRAINING_AREAS)


class WorkoutItem(models.Model):
    class Meta:
        verbose_name = "トレーニング種目"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    training_name = models.CharField(verbose_name="トレーニング種目", max_length=64)
    category = models.ForeignKey(TrainingArea, on_delete=models.CASCADE)


class WorkoutFeeling(models.Model):
    FEEL_TOOEASY = "too_easy"
    FEEL_EASY = "easy"
    FEEL_NORMAL = "normal"
    FEEL_HARD = "hard"
    FEEL_TOO_HARD = "too_hard"
    FEEL_CANNOT = "cannot"

    FEELS = (
        (FEEL_TOOEASY, _("簡単すぎ")),
        (FEEL_EASY, _("簡単")),
        (FEEL_NORMAL, _("普通")),
        (FEEL_HARD, _("きつい")),
        (FEEL_TOO_HARD, _("キツすぎ")),
        (FEEL_CANNOT, _("無理")),
    )

    class Meta:
        verbose_name = "ワークアウト時の感想"
        ordering = ["feel"]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    feel = models.CharField(verbose_name="ワークアウト感想", max_length=64, choices=FEELS)


class Condition(models.Model):
    FEEL_BEST = "best"
    FEEL_BETTER = "better"
    FEEL_NORMAL = "normal"
    FEEL_BAD = "bad"
    FEEL_SO_BAD = "so_bad"
    FEEL_CANNOT = "cannot"

    FEELS = (
        (FEEL_BEST, _("最高！")),
        (FEEL_BETTER, _("いい感じ")),
        (FEEL_NORMAL, _("普通")),
        (FEEL_BAD, _("良くはない")),
        (FEEL_SO_BAD, _("悪い")),
        (FEEL_CANNOT, _("無理")),
    )

    class Meta:
        verbose_name = "ワークアウトセッションのコンディション"


class WorkoutSession(models.Model):
    class Meta:
        verbose_name = "ワークアウトセッション"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    started_at = models.DateTimeField(verbose_name="トレーニング開始日時", auto_now_add=True)
    finished_at = models.DateTimeField(verbose_name="トレーニング終了日時", null=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)


class Workout(models.Model):
    class Meta:
        verbose_name = "トレーニング"
        ordering = ["-trained_at"]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    training_item = models.ForeignKey(WorkoutItem, on_delete=models.CASCADE)
    feeling = models.ForeignKey(WorkoutFeeling, on_delete=models.CASCADE)
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)

    rep_count = models.IntegerField(verbose_name="レップ数")
    set_count = models.IntegerField(verbose_name="セット数")
    weight_kg = models.FloatField(verbose_name="重さ(kg)")

    trained_at = models.DateTimeField(verbose_name="トレーニング日時", auto_now_add=True)
