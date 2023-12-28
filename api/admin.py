from django.contrib import admin

from api.models.training import TrainingArea, WorkoutItem

# Register your models here.
admin.site.register(TrainingArea)
admin.site.register(WorkoutItem)
