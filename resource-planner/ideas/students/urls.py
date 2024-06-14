from django.urls import path
from . import views

# app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('all_students/', views.all_students, name='all_students'),
    path('all_students/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]