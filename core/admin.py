from django.contrib import admin
from .models import CustomUser, Contributer, ProjectCreator, Project, FieldOfScience, ContributedProject, RecommendedProject, SimilarUser

admin.site.register(CustomUser)
admin.site.register(Contributer)
admin.site.register(ProjectCreator)
admin.site.register(Project)
admin.site.register(FieldOfScience)
admin.site.register(ContributedProject)
admin.site.register(RecommendedProject)
admin.site.register(SimilarUser)