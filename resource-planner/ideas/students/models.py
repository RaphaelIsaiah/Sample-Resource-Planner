from django.db import models

# Create your models here.

class Student(models.Model):
    COURSES = [
        ('AI', 'Professional Diploma in Artificial Intelligence'),
        ('IT', 'Professional Diploma in Data Analytics'),
        ('ECE', 'Professional Diploma in Software Engineering'),
        ('ME', 'Professional Diploma in Blockchain Technology'),
    ]

    student_id = models.CharField(max_length=150, unique=True)
    names = models.CharField(max_length=150)
    course = models.CharField(max_length=10, choices=COURSES)
    email_address = models.EmailField(unique=True)
    phone_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=250, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.names
