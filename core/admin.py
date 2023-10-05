from django.contrib import admin
<<<<<<< HEAD
from .models import CustomUser, Contributer, ProjectCreator, Project
admin.site.register(Contributer)
admin.site.register(ProjectCreator)
admin.site.register(Project)
=======
from .models import CustomUser, Contributer, ProjectCreator, Project, FieldOfScience, ContributedProject, RecommendedProject, SimilarUser

admin.site.register(CustomUser)
admin.site.register(Contributer)
admin.site.register(ProjectCreator)
admin.site.register(Project)
admin.site.register(FieldOfScience)
admin.site.register(ContributedProject)
admin.site.register(RecommendedProject)
admin.site.register(SimilarUser)
>>>>>>> 8881ba0130c9b651f6df105bb8e38c9b08f3b196
