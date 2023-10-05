from django.contrib import admin
from .models import CustomUser, Contributer, ProjectCreator, Project

admin.site.register(Contributer)
admin.site.register(ProjectCreator)
admin.site.register(Project)
