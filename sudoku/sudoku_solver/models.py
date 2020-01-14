from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Results(models.Model):
    student_name = models.CharField(max_length=100)
    task_selected = models.CharField(max_length=100)
    age = models.IntegerField()
    stamp = models.DateTimeField(default=now,editable=False)
    task_outcome = models.CharField(max_length=20)
    
