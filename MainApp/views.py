from django.shortcuts import render, HttpResponse
from .models import Project

# Home page view route
def home(request):
  
  return render(request, 'MainApp/home.html')

# Project page view route
def projects(request):
  projects = Project.objects.all()
  context = {"projects": projects}
  return render(request, 'MainApp/project.html', context)

# About page view route
def about(request):
  return render(request, 'MainApp/about.html')
