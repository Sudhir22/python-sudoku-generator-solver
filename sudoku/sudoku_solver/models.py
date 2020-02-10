from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Results(models.Model):
    time_taken = models.CharField(max_length=10,null=True)
    task_selected = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    stamp = models.DateTimeField(default=now,editable=False)
    task_outcome = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,null=True)
    subjects = models.CharField(max_length=10,null=True)
    favorite = models.CharField(max_length=10,null=True)
    standard = models.CharField(max_length=10,null=True)
    task1_selection = models.IntegerField(null=True)
    task2_selection = models.IntegerField(null=True)
    task2_colour = models.CharField(max_length=10,null=True)
    token = models.CharField(max_length=10,null=True)
    age_2 = models.CharField(max_length=10,null=True)
    gender_2 = models.CharField(max_length=10,null=True)
    subjects_2 = models.CharField(max_length=10,null=True)
    favorite_2 = models.CharField(max_length=10,null=True)
    standard_2 = models.CharField(max_length=10,null=True)
