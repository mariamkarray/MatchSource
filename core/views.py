from django.shortcuts import render
from django.http import HttpResponse
from . import models

def register(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def recommendProjectsForUser(request):
    user = models.Contributer.objects.get(id=request.user.id)
    recommended_projects = user.recommended_projects.all()
    if len(recommended_projects) != 0:
        # compute recommended projects
        recommended_projects = 1
        for project in recommended_projects:
            models.RecommendedProject.objects.create(user=user, project=project)
#user id and i will get the user
    #request extract model User
    #does this user have a recommended project list, if yes call db, if not compute
    #user.skills
#str+str+str
#call data science function#
# list of arkam list of project_ids 
#save fel database
#send to the user

def recommendUserForProjects(request):
    print("hello")
    #project_id
    #does this project have a recommended user list, if yes call db, if not compute
    #project.skills
#str+str+str
#get_projects(str+str+str)
#call data science function
#list of arkam list of user_ids
#save fel database
#send to the user