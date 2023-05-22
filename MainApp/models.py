from django.db import models


# projects model
class Project(models.Model):
  projectName = models.CharField(max_length=100)
  date_uploaded = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  project_link = models.URLField(null=True, blank=True)

  def __str__(self):
      return self.projectName
  