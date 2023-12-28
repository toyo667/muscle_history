from django.contrib import admin
from api.models.master import WorkoutFeeling, Condition, TrainingArea

from api.models.training import Workout, WorkoutItem, WorkoutSession

# Register your models here.
admin.site.register(TrainingArea)
admin.site.register(WorkoutFeeling)
admin.site.register(Condition)

admin.site.register(WorkoutItem)
admin.site.register(WorkoutSession)
admin.site.register(Workout)
