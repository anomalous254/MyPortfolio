from django.contrib import admin
from .models import Project, About, Achievements

# Registering about db model
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("name", "location", 'phone', 'degree','course','school','study','freelance')

# Registering achievments db model
@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('projects', 'clients', 'stars')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("projectName", "project_link")

