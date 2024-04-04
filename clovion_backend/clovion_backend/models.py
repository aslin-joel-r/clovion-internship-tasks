from django.db import models

class StudentMarks(models.Model):
    # Define your model fields here
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()

    class Meta:
        # Explicitly specify the app_label for the model
        app_label = 'clovion_backend'
