from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class registermodel(User):
    dor=models.DateTimeField(default=timezone.now)


class exam_model(models.Model):
    select_user = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    questions = models.CharField(max_length=200)
    inputs = models.CharField(max_length=200)