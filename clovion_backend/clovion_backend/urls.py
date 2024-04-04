
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.enter_marks, name='enter-marks'),
    path('result/', views.result, name='result'),
]
