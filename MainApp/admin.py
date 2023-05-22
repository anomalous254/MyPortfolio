from django.contrib import admin
from .models import Project, About, Achievements

# Registering project db model
admin.site.register(Project)

# Registering about db model
admin.site.register(About)

# Registering achievments db model
admin.site.register(Achievements)

