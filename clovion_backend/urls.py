# urls.py
from django.urls import path
from .views import enter_marks

urlpatterns = [
    path('enter-marks/', enter_marks, name='enter-marks'),
    # Add other URL patterns as needed
]
