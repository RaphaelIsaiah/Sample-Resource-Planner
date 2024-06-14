from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.

# This makes the the html pages display.

def all_students(request):
  allstudents = Student.objects.all().values()
  template = loader.get_template('all_students.html')
  context = {
    'allstudents': allstudents,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  allstudents = Student.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'allstudents': allstudents,
  }
  return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))