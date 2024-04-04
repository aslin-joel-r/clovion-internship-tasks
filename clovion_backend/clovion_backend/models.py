# models.py
from django.db import models

class StudentMarks(models.Model):
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total_marks = models.IntegerField(blank=True, null=True)  # Add new field for total marks
    average_marks = models.FloatField(blank=True, null=True)  # Add new field for average marks
