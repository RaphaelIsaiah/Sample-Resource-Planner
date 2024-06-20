from django.contrib import admin
from .models import Student, Attendance

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_display = ("names", "student_id", "course", "location")
  search_fields = ['__all__']

class AttendanceAdmin(admin.ModelAdmin):
  list_display = ("student_id", "student_name", "date")
  search_fields = ['__all__']



admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.site_header = 'IDEAS ADMINISTRATION'