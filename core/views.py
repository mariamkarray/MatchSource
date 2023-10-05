from django.http import HttpResponse
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import Contributer, Project, ProjectCreator
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from datetime import date
from clustering import get_cluster, cluster_paragraphs


User = get_user_model()

class SignUpForm(UserCreationForm):
    birthdate = forms.DateField(required=False)
    skills = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    participation_tasks = forms.ModelMultipleChoiceField(queryset=Project.objects.all(), required=False)  
     

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

# def importUsers(request):
#     contributers_data = [
#         {
#             "name": "John Scientist",
#             "email": "john.scientist@example.com",
#             "username": "johnscientist",
#             "password": "password123",
#             "birthdate": date(1980, 5, 12),
#             "skills": "Research, Data Analysis, Field Work",
#             "description": "I am a passionate scientist with expertise in environmental science.",
#             "participation_tasks": "Collecting water samples, Analyzing data, Writing research papers",
#             "fields_of_science": "Environmental Science, Ecology",
#         },
#         {
#             "name": "Jane Researcher",
#             "email": "jane.researcher@example.com",
#             "username": "janeresearcher",
#             "password": "securepass456",
#             "birthdate": date(1985, 8, 22),
#             "skills": "Laboratory Research, Data Visualization, Statistical Analysis",
#             "description": "I specialize in conducting experiments and analyzing data.",
#             "participation_tasks": "Running lab experiments, Creating data visualizations",
#             "fields_of_science": "Biology, Chemistry",
#         },
#         {
#             "name": "David Eco Enthusiast",
#             "email": "david.eco@example.com",
#             "username": "davideco",
#             "password": "eco123pass",
#             "birthdate": date(1992, 3, 7),
#             "skills": "Conservation, Wildlife Tracking, Environmental Education",
#             "description": "I am dedicated to preserving our natural world and educating others about it.",
#             "participation_tasks": "Tracking wildlife, Leading nature workshops",
#             "fields_of_science": "Conservation Biology, Ecology",
#         },
#         {
#             "name": "Sarah Geologist",
#             "email": "sarah.geologist@example.com",
#             "username": "sarahgeologist",
#             "password": "rocklover789",
#             "birthdate": date(1988, 11, 15),
#             "skills": "Geological Mapping, Rock Analysis, Seismology",
#             "description": "I explore the Earth's crust and study geological phenomena.",
#             "participation_tasks": "Mapping geological formations, Studying rock samples",
#             "fields_of_science": "Geology, Earth Sciences",
#         },
#         {
#             "name": "Michael Astronomer",
#             "email": "michael.astronomer@example.com",
#             "username": "michaelastronomer",
#             "password": "cosmicpass321",
#             "birthdate": date(1975, 9, 28),
#             "skills": "Telescope Observation, Celestial Phenomena Analysis, Astrophotography",
#             "description": "I observe and study objects in the universe beyond our planet.",
#             "participation_tasks": "Observing stars, Capturing images of galaxies",
#             "fields_of_science": "Astronomy, Astrophysics",
#         }
#     ]
#     contributers_data += [
#         {
#             "name": "Laura Oceanographer",
#             "email": "laura.ocean@example.com",
#             "username": "lauraocean",
#             "password": "ocean123pass",
#             "birthdate": date(1984, 6, 18),
#             "skills": "Marine Biology, Oceanographic Research, Diving",
#             "description": "I explore the mysteries of the ocean and study marine life.",
#             "participation_tasks": "Conducting underwater research, Collecting samples",
#             "fields_of_science": "Oceanography, Marine Biology",
#         },
#         {
#             "name": "Alex Environmentalist",
#             "email": "alex.environment@example.com",
#             "username": "alexenvironment",
#             "password": "greenearth456",
#             "birthdate": date(1990, 2, 9),
#             "skills": "Sustainability, Conservation, Environmental Advocacy",
#             "description": "I'm passionate about protecting the environment and promoting sustainability.",
#             "participation_tasks": "Organizing eco-friendly events, Raising awareness",
#             "fields_of_science": "Environmental Science, Conservation",
#         },
#         {
#             "name": "Daniel Botanist",
#             "email": "daniel.botanist@example.com",
#             "username": "danielbotanist",
#             "password": "plantsrule789",
#             "birthdate": date(1982, 4, 25),
#             "skills": "Plant Taxonomy, Botanical Research, Herbarium Collection",
#             "description": "I study plants, their taxonomy, and their ecological roles.",
#             "participation_tasks": "Identifying plant species, Creating herbarium collections",
#             "fields_of_science": "Botany, Ecology",
#         },
#         {
#             "name": "Emily Wildlife Biologist",
#             "email": "emily.wildlife@example.com",
#             "username": "emilywildlife",
#             "password": "wildlife321pass",
#             "birthdate": date(1987, 8, 12),
#             "skills": "Wildlife Conservation, Field Research, Animal Behavior",
#             "description": "I'm dedicated to studying and conserving wildlife species.",
#             "participation_tasks": "Tracking animal behavior, Conducting field surveys",
#             "fields_of_science": "Wildlife Biology, Conservation",
#         },
#         {
#             "name": "Thomas Meteorologist",
#             "email": "thomas.meteorologist@example.com",
#             "username": "thomasweather",
#             "password": "stormchaser123",
#             "birthdate": date(1979, 3, 3),
#             "skills": "Weather Forecasting, Climate Analysis, Storm Chasing",
#             "description": "I analyze weather patterns and study the Earth's climate.",
#             "participation_tasks": "Forecasting weather, Chasing storms",
#             "fields_of_science": "Meteorology, Climate Science",
#         },
#         {
#             "name": "Sophia Ecologist",
#             "email": "sophia.ecologist@example.com",
#             "username": "sophiaecology",
#             "password": "ecosystems456",
#             "birthdate": date(1986, 11, 30),
#             "skills": "Ecosystem Analysis, Biodiversity Conservation, Habitat Restoration",
#             "description": "I explore and restore ecosystems to promote biodiversity.",
#             "participation_tasks": "Restoring habitats, Studying ecosystems",
#             "fields_of_science": "Ecology, Conservation",
#         },
#         {
#             "name": "William Geophysicist",
#             "email": "william.geo@example.com",
#             "username": "williamgeophysics",
#             "password": "earthquake789",
#             "birthdate": date(1981, 7, 8),
#             "skills": "Seismic Data Analysis, Earthquake Research, Geophysical Surveys",
#             "description": "I investigate seismic activities and study the Earth's structure.",
#             "participation_tasks": "Analyzing seismic data, Conducting geophysical surveys",
#             "fields_of_science": "Geophysics, Seismology",
#         },
#         {
#             "name": "Olivia Ornithologist",
#             "email": "olivia.ornithologist@example.com",
#             "username": "oliviaornitho",
#             "password": "birdlover123",
#             "birthdate": date(1983, 5, 14),
#             "skills": "Bird Watching, Avian Research, Bird Conservation",
#             "description": "I observe and study birds, their behavior, and habitats.",
#             "participation_tasks": "Bird watching, Nest monitoring",
#             "fields_of_science": "Ornithology, Avian Ecology",
#         },
#         {
#             "name": "Matthew Archaeologist",
#             "email": "matthew.archaeologist@example.com",
#             "username": "matthewarcheo",
#             "password": "ancientcivilizations456",
#             "birthdate": date(1980, 9, 22),
#             "skills": "Archaeological Excavations, Artifact Analysis, Cultural Heritage",
#             "description": "I dig into the past, uncovering ancient civilizations and their artifacts.",
#             "participation_tasks": "Excavating archaeological sites, Analyzing artifacts",
#             "fields_of_science": "Archaeology, Cultural Heritage",
#         },
#         {
#             "name": "Ella Entomologist",
#             "email": "ella.entomologist@example.com",
#             "username": "ellaentomo",
#             "password": "buglover789",
#             "birthdate": date(1989, 12, 7),
#             "skills": "Insect Taxonomy, Entomological Research, Bug Collection",
#             "description": "I study the fascinating world of insects and their roles in ecosystems.",
#             "participation_tasks": "Collecting insect specimens, Identifying insect species",
#             "fields_of_science": "Entomology, Ecology",
#         }
#     ]

    
#     for contributer_data in contributers_data[:1]:
#         contributer = Contributer.objects.create(
        
#             name=contributer_data["name"],
#             email=contributer_data["email"],
#             username=contributer_data["username"],
#             password=contributer_data["password"],
#             birthdate=contributer_data["birthdate"],
#             skills=contributer_data["skills"],
#             description=contributer_data["description"],
#             participation_tasks=contributer_data["participation_tasks"],
#             fields_of_science=contributer_data["fields_of_science"],
#         )



# def importProjects(request):
#     import pandas as pd
#     df = pd.read_csv('feed.csv')

#     for index, row in df.iterrows():
#         Project.objects.create(
#             name=row['project_name'],
#             creator=ProjectCreator.objects.get(id=17),
#             description=row['project_description'],
#             skills=[],
#             fields_of_science=row['fields_of_science'],
#             keywords=row['keywords'],
#             project_status=row['project_status'],
#             agency_sponsor=row['agency_sponsor'],
#             agency_sponsor_other=row['agency_sponsor_other'],
#             geographic_scope=row['geographic_scope'],
#             participant_age=row['participant_age'],
#             project_goals=row['project_goals'],
#             scistarter_url=row['scistarter'],
#             email=row['email'],
#             project_url_on_catalog=row['project_url_on_catalog'],
#             project_url_external=row['project_url_external'],
#             cluster_id= -1
#         )

# def assign_clusters_to_projects(request):
#     projects = Project.objects.all()
#     paragraphs = []
#     for project in projects:
#         paragraph = project.description + ' ' + project.participation_tasks + ' ' + project.keywords + ' ' + project.fields_of_science 
#         paragraphs.append(paragraph)


#     _,_, clusters = cluster_paragraphs(paragraphs)

#     for project_id, cluster_id in clusters:
#         project = Project.objects.get(id=project_id + 1)
#         project.cluster_id = cluster_id
#         project.save()

#     return HttpResponse("Done")
