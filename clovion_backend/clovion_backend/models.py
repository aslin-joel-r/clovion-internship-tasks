# models.py
from django.db import models

class StudentMarks(models.Model):
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
