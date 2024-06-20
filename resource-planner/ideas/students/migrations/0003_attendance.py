# Generated by Django 5.0.6 on 2024-06-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_date_student_gender_student_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=150, unique=True)),
                ('date', models.DateTimeField(unique=True)),
                ('student_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
    ]