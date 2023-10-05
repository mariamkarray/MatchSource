from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import Contributer, Project, FieldOfScience, ProjectCreator
from django.contrib.auth.forms import AuthenticationForm
from django import forms
User = get_user_model()

class SignUpForm(UserCreationForm):
    birthdate = forms.DateField(required=False)
    skills = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    participation_tasks = forms.ModelMultipleChoiceField(queryset=Project.objects.all(), required=False)  
    fields_of_science = forms.ModelMultipleChoiceField(queryset=FieldOfScience.objects.all(), required=False)
     

    class Meta:
        model = Contributer
        fields = ('username', 'password1', 'email', 'birthdate', 'skills', 'description', 'participation_tasks', 'fields_of_science')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Contributer   
        
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def index(request):
    return render(request, 'index.html')

# def relevantProjects()

