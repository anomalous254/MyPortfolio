from django.db import models


# projects db model
class Project(models.Model):
  projectName = models.CharField(max_length=100)
  date_uploaded = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  project_link = models.URLField(null=True, blank=True)

  def __str__(self):
      return self.projectName
    
    
# About db model
class About(models.Model):
  name = models.CharField(max_length=100, default='Peter Nyando')
  website = models.URLField(null=True, blank=True)
  location = models.CharField(max_length=100)
  phone = models.CharField(max_length=100, default='+254')
  freelance = models.CharField(max_length=100)
  degree = models.CharField(max_length=100)
  course = models.CharField(max_length=100)
  school = models.CharField(max_length=100)
  study = models.CharField(max_length=100)
  about = models.TextField(default='About')
  
  def __str__(self):
      return self.name
    
    
# Achievements db model
class Achievements(models.Model):
  projects = models.CharField(max_length=100)
  clients = models.CharField(max_length=100)
  stars = models.CharField(max_length=100)
  

  