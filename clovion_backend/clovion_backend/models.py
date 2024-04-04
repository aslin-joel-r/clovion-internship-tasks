# models.py
from django.db import models

class StudentMarks(models.Model):
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total_marks = models.IntegerField(blank=True, null=True)  
    average_marks = models.FloatField(blank=True, null=True)  
