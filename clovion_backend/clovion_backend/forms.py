# forms.py
from django import forms
from .models import StudentMarks

class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = '__all__'
