from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Results(models.Model):
    time_taken = models.CharField(max_length=10,null=True)
    task_selected = models.CharField(max_length=50)
    age = models.IntegerField()
    stamp = models.DateTimeField(default=now,editable=False)
    task_outcome = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,null=True)
    standard = models.CharField(max_length=10,null=True)
    task1_selection = models.IntegerField(null=True)
    task2_selection = models.IntegerField(null=True)
    task2_colour = models.CharField(max_length=10,null=True)

