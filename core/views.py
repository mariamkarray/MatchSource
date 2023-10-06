from django.http import HttpResponse
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import Contributer, Project, ProjectCreator, CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from datetime import date
from datetime import date
from clustering import get_cluster, cluster_paragraphs
import pandas as pd

User = get_user_model()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
class SignUpForm(UserCreationForm):
    description = forms.CharField(widget=forms.Textarea, required=True)
    skills = forms.CharField(max_length=255, required=True)
    participation_tasks = forms.CharField(widget=forms.Textarea, required=True) 
     

    class Meta:
        model = Contributer
        fields = ('username', 'password1', 'email', 'birthdate', 'skills', 'description', 'participation_tasks', 'fields_of_science', 'contributed_projects')
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser    
        
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            user.recommended_projects = recommened_projects_for_user(request)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def loginView(request):
    form = LoginForm(request=request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                print(f"User type: {type(user)}")

                login(request, user)
                return render(request, 'home.html', {'similar_projects': []})
            else:
                form = LoginForm()
            
    return render(request, 'login.html', {'form': form})

def index(request):
    dt = pd.DataFrame(list(models.Contributer.objects.all().values()))
    dt.to_csv('users.csv')
    return render(request, 'index.html')

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return render(request, 'index.html')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})

def recommendProjectsForUser(request):
    user = models.Contributer.objects.get(id=request.user.id)
    recommended_projects = user.recommended_projects.all()
    if len(recommended_projects) != 0:
        # compute recommended projects
        recommended_projects = 1
        for project in recommended_projects:
            models.RecommendedProject.objects.create(user=user, project=project)

def recommened_projects_for_user(request):
    user=models.CustomUser.objects.get(id=1)
    contributer=models.Contributer.objects.get(id=user.id)
    no = contributer.description + ' ' + contributer.skills
    cluster_id = get_cluster(no, 'no', 0)
    similar_projects = Project.objects.filter(cluster_id=cluster_id)
    return HttpResponse(similar_projects) 

def moot(request):
    user=models.CustomUser.objects.get(id=1)
    contributer=models.Contributer.objects.get(id=user.id)
    no = contributer.description + ' ' + contributer.skills
    cluster_id = get_cluster(no, 'no', 0)
    similar_projects = Project.objects.filter(cluster_id=cluster_id)
    return HttpResponse(similar_projects) 