from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 独自のフィールドを追加
    # email = models.EmailField(unique=True)
    # # date_of_birth = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username
