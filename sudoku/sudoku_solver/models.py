from django.db import models

# Create your models here.

class Results(models.Model):
    student_name = models.CharField(max_length=100)
    task_selected = models.CharField(max_length=100)
    age = models.IntegerField()
    task_outcome = models.CharField(max_length=20)
    
