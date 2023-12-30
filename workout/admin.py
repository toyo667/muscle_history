from django.contrib import admin
from workout.models.master import WorkoutFeeling, Condition, TrainingArea

from django.contrib.auth.admin import UserAdmin
from workout.models.training import Workout, WorkoutItem, WorkoutSession

# Register your models here.
admin.site.register(TrainingArea)
admin.site.register(WorkoutFeeling)
admin.site.register(Condition)

admin.site.register(WorkoutItem)
admin.site.register(WorkoutSession)
admin.site.register(Workout)
