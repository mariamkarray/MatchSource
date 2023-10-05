from django.http import HttpResponse
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL you want to redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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

def importUsers():
    contributers_data = [
    {
        "name": "John Scientist",
        "email": "john.scientist@example.com",
        "username": "johnscientist",
        "password": "password123",
        "birthdate": date(1980, 5, 12),
        "skills": "Research, Data Analysis, Field Work",
        "description": "I am a passionate scientist with expertise in environmental science.",
        "participation_tasks": "Collecting water samples, Analyzing data, Writing research papers",
        "fields_of_science": "Environmental Science, Ecology",
    },
    {
        "name": "Jane Researcher",
        "email": "jane.researcher@example.com",
        "username": "janeresearcher",
        "password": "securepass456",
        "birthdate": date(1985, 8, 22),
        "skills": "Laboratory Research, Data Visualization, Statistical Analysis",
        "description": "I specialize in conducting experiments and analyzing data.",
        "participation_tasks": "Running lab experiments, Creating data visualizations",
        "fields_of_science": "Biology, Chemistry",
    },
    {
        "name": "David Eco Enthusiast",
        "email": "david.eco@example.com",
        "username": "davideco",
        "password": "eco123pass",
        "birthdate": date(1992, 3, 7),
        "skills": "Conservation, Wildlife Tracking, Environmental Education",
        "description": "I am dedicated to preserving our natural world and educating others about it.",
        "participation_tasks": "Tracking wildlife, Leading nature workshops",
        "fields_of_science": "Conservation Biology, Ecology",
    },
    {
        "name": "Sarah Geologist",
        "email": "sarah.geologist@example.com",
        "username": "sarahgeologist",
        "password": "rocklover789",
        "birthdate": date(1988, 11, 15),
        "skills": "Geological Mapping, Rock Analysis, Seismology",
        "description": "I explore the Earth's crust and study geological phenomena.",
        "participation_tasks": "Mapping geological formations, Studying rock samples",
        "fields_of_science": "Geology, Earth Sciences",
    },
    {
        "name": "Michael Astronomer",
        "email": "michael.astronomer@example.com",
        "username": "michaelastronomer",
        "password": "cosmicpass321",
        "birthdate": date(1975, 9, 28),
        "skills": "Telescope Observation, Celestial Phenomena Analysis, Astrophotography",
        "description": "I observe and study objects in the universe beyond our planet.",
        "participation_tasks": "Observing stars, Capturing images of galaxies",
        "fields_of_science": "Astronomy, Astrophysics",
    }
]
    contributers_data += [
        {
            "name": "Laura Oceanographer",
            "email": "laura.ocean@example.com",
            "username": "lauraocean",
            "password": "ocean123pass",
            "birthdate": date(1984, 6, 18),
            "skills": "Marine Biology, Oceanographic Research, Diving",
            "description": "I explore the mysteries of the ocean and study marine life.",
            "participation_tasks": "Conducting underwater research, Collecting samples",
            "fields_of_science": "Oceanography, Marine Biology",
        },
        {
            "name": "Alex Environmentalist",
            "email": "alex.environment@example.com",
            "username": "alexenvironment",
            "password": "greenearth456",
            "birthdate": date(1990, 2, 9),
            "skills": "Sustainability, Conservation, Environmental Advocacy",
            "description": "I'm passionate about protecting the environment and promoting sustainability.",
            "participation_tasks": "Organizing eco-friendly events, Raising awareness",
            "fields_of_science": "Environmental Science, Conservation",
        },
        {
            "name": "Daniel Botanist",
            "email": "daniel.botanist@example.com",
            "username": "danielbotanist",
            "password": "plantsrule789",
            "birthdate": date(1982, 4, 25),
            "skills": "Plant Taxonomy, Botanical Research, Herbarium Collection",
            "description": "I study plants, their taxonomy, and their ecological roles.",
            "participation_tasks": "Identifying plant species, Creating herbarium collections",
            "fields_of_science": "Botany, Ecology",
        },
        {
            "name": "Emily Wildlife Biologist",
            "email": "emily.wildlife@example.com",
            "username": "emilywildlife",
            "password": "wildlife321pass",
            "birthdate": date(1987, 8, 12),
            "skills": "Wildlife Conservation, Field Research, Animal Behavior",
            "description": "I'm dedicated to studying and conserving wildlife species.",
            "participation_tasks": "Tracking animal behavior, Conducting field surveys",
            "fields_of_science": "Wildlife Biology, Conservation",
        },
        {
            "name": "Thomas Meteorologist",
            "email": "thomas.meteorologist@example.com",
            "username": "thomasweather",
            "password": "stormchaser123",
            "birthdate": date(1979, 3, 3),
            "skills": "Weather Forecasting, Climate Analysis, Storm Chasing",
            "description": "I analyze weather patterns and study the Earth's climate.",
            "participation_tasks": "Forecasting weather, Chasing storms",
            "fields_of_science": "Meteorology, Climate Science",
        },
        {
            "name": "Sophia Ecologist",
            "email": "sophia.ecologist@example.com",
            "username": "sophiaecology",
            "password": "ecosystems456",
            "birthdate": date(1986, 11, 30),
            "skills": "Ecosystem Analysis, Biodiversity Conservation, Habitat Restoration",
            "description": "I explore and restore ecosystems to promote biodiversity.",
            "participation_tasks": "Restoring habitats, Studying ecosystems",
            "fields_of_science": "Ecology, Conservation",
        },
        {
            "name": "William Geophysicist",
            "email": "william.geo@example.com",
            "username": "williamgeophysics",
            "password": "earthquake789",
            "birthdate": date(1981, 7, 8),
            "skills": "Seismic Data Analysis, Earthquake Research, Geophysical Surveys",
            "description": "I investigate seismic activities and study the Earth's structure.",
            "participation_tasks": "Analyzing seismic data, Conducting geophysical surveys",
            "fields_of_science": "Geophysics, Seismology",
        },
        {
            "name": "Olivia Ornithologist",
            "email": "olivia.ornithologist@example.com",
            "username": "oliviaornitho",
            "password": "birdlover123",
            "birthdate": date(1983, 5, 14),
            "skills": "Bird Watching, Avian Research, Bird Conservation",
            "description": "I observe and study birds, their behavior, and habitats.",
            "participation_tasks": "Bird watching, Nest monitoring",
            "fields_of_science": "Ornithology, Avian Ecology",
        },
        {
            "name": "Matthew Archaeologist",
            "email": "matthew.archaeologist@example.com",
            "username": "matthewarcheo",
            "password": "ancientcivilizations456",
            "birthdate": date(1980, 9, 22),
            "skills": "Archaeological Excavations, Artifact Analysis, Cultural Heritage",
            "description": "I dig into the past, uncovering ancient civilizations and their artifacts.",
            "participation_tasks": "Excavating archaeological sites, Analyzing artifacts",
            "fields_of_science": "Archaeology, Cultural Heritage",
        },
        {
            "name": "Ella Entomologist",
            "email": "ella.entomologist@example.com",
            "username": "ellaentomo",
            "password": "buglover789",
            "birthdate": date(1989, 12, 7),
            "skills": "Insect Taxonomy, Entomological Research, Bug Collection",
            "description": "I study the fascinating world of insects and their roles in ecosystems.",
            "participation_tasks": "Collecting insect specimens, Identifying insect species",
            "fields_of_science": "Entomology, Ecology",
        }
    ]
    contributers_data += [
    {
        "name": "Laura Oceanographer",
        "email": "laura.ocean@example.com",
        "username": "lauraocean",
        "password": "ocean123pass",
        "birthdate": date(1984, 6, 18),
        "skills": "Marine Biology, Oceanographic Research, Diving",
        "description": "I explore the mysteries of the ocean and study marine life.",
        "participation_tasks": "Conducting underwater research, Collecting samples",
        "fields_of_science": "Oceanography, Marine Biology",
    },
    {
        "name": "Alex Environmentalist",
        "email": "alex.environment@example.com",
        "username": "alexenvironment",
        "password": "greenearth456",
        "birthdate": date(1990, 2, 9),
        "skills": "Sustainability, Conservation, Environmental Advocacy",
        "description": "I'm passionate about protecting the environment and promoting sustainability.",
        "participation_tasks": "Organizing eco-friendly events, Raising awareness",
        "fields_of_science": "Environmental Science, Conservation",
    },
    {
        "name": "Daniel Botanist",
        "email": "daniel.botanist@example.com",
        "username": "danielbotanist",
        "password": "plantsrule789",
        "birthdate": date(1982, 4, 25),
        "skills": "Plant Taxonomy, Botanical Research, Herbarium Collection",
        "description": "I study plants, their taxonomy, and their ecological roles.",
        "participation_tasks": "Identifying plant species, Creating herbarium collections",
        "fields_of_science": "Botany, Ecology",
    },
    {
        "name": "Emily Wildlife Biologist",
        "email": "emily.wildlife@example.com",
        "username": "emilywildlife",
        "password": "wildlife321pass",
        "birthdate": date(1987, 8, 12),
        "skills": "Wildlife Conservation, Field Research, Animal Behavior",
        "description": "I'm dedicated to studying and conserving wildlife species.",
        "participation_tasks": "Tracking animal behavior, Conducting field surveys",
        "fields_of_science": "Wildlife Biology, Conservation",
    },
    {
        "name": "Thomas Meteorologist",
        "email": "thomas.meteorologist@example.com",
        "username": "thomasweather",
        "password": "stormchaser123",
        "birthdate": date(1979, 3, 3),
        "skills": "Weather Forecasting, Climate Analysis, Storm Chasing",
        "description": "I analyze weather patterns and study the Earth's climate.",
        "participation_tasks": "Forecasting weather, Chasing storms",
        "fields_of_science": "Meteorology, Climate Science",
    },
    {
        "name": "Sophia Ecologist",
        "email": "sophia.ecologist@example.com",
        "username": "sophiaecology",
        "password": "ecosystems456",
        "birthdate": date(1986, 11, 30),
        "skills": "Ecosystem Analysis, Biodiversity Conservation, Habitat Restoration",
        "description": "I explore and restore ecosystems to promote biodiversity.",
        "participation_tasks": "Restoring habitats, Studying ecosystems",
        "fields_of_science": "Ecology, Conservation",
    },
    {
        "name": "William Geophysicist",
        "email": "william.geo@example.com",
        "username": "williamgeophysics",
        "password": "earthquake789",
        "birthdate": date(1981, 7, 8),
        "skills": "Seismic Data Analysis, Earthquake Research, Geophysical Surveys",
        "description": "I investigate seismic activities and study the Earth's structure.",
        "participation_tasks": "Analyzing seismic data, Conducting geophysical surveys",
        "fields_of_science": "Geophysics, Seismology",
    },
    {
        "name": "Olivia Ornithologist",
        "email": "olivia.ornithologist@example.com",
        "username": "oliviaornitho",
        "password": "birdlover123",
        "birthdate": date(1983, 5, 14),
        "skills": "Bird Watching, Avian Research, Bird Conservation",
        "description": "I observe and study birds, their behavior, and habitats.",
        "participation_tasks": "Bird watching, Nest monitoring",
        "fields_of_science": "Ornithology, Avian Ecology",
    },
    {
        "name": "Matthew Archaeologist",
        "email": "matthew.archaeologist@example.com",
        "username": "matthewarcheo",
        "password": "ancientcivilizations456",
        "birthdate": date(1980, 9, 22),
        "skills": "Archaeological Excavations, Artifact Analysis, Cultural Heritage",
        "description": "I dig into the past, uncovering ancient civilizations and their artifacts.",
        "participation_tasks": "Excavating archaeological sites, Analyzing artifacts",
        "fields_of_science": "Archaeology, Cultural Heritage",
    },
    {
        "name": "Ella Entomologist",
        "email": "ella.entomologist@example.com",
        "username": "ellaentomo",
        "password": "buglover789",
        "birthdate": date(1989, 12, 7),
        "skills": "Insect Taxonomy, Entomological Research, Bug Collection",
        "description": "I study the fascinating world of insects and their roles in ecosystems.",
        "participation_tasks": "Collecting insect specimens, Identifying insect species",
        "fields_of_science": "Entomology, Ecology",
    },
    {
        "name": "Sophia Environmental Scientist",
        "email": "sophia.environment@example.com",
        "username": "sophiaenvironment",
        "password": "science123",
        "birthdate": date(1992, 4, 3),
        "skills": "Environmental Impact Assessment, Pollution Control, Sustainability",
        "description": "I work to mitigate the environmental impact of human activities.",
        "participation_tasks": "Conducting environmental assessments, Promoting sustainability",
        "fields_of_science": "Environmental Science, Sustainability",
    },
    {
        "name": "James Astrophysicist",
        "email": "james.astro@example.com",
        "username": "jamesastro",
        "password": "cosmos789",
        "birthdate": date(1984, 9, 15),
        "skills": "Stellar Physics, Galaxy Formation, Cosmology",
        "description": "I explore the universe's mysteries, from stars to galaxies.",
        "participation_tasks": "Studying celestial objects, Analyzing astronomical data",
        "fields_of_science": "Astrophysics, Cosmology",
    },
    {
        "name": "Ava Microbiologist",
        "email": "ava.microbio@example.com",
        "username": "avamicro",
        "password": "microbes123",
        "birthdate": date(1988, 7, 27),
        "skills": "Microbial Ecology, Pathogen Research, Laboratory Techniques",
        "description": "I delve into the microscopic world of bacteria and microbes.",
        "participation_tasks": "Conducting microbial research, Identifying pathogens",
        "fields_of_science": "Microbiology, Ecology",
    },
    {
        "name": "Logan Geologist",
        "email": "logan.geologist@example.com",
        "username": "logangeo",
        "password": "rocks456",
        "birthdate": date(1983, 2, 10),
        "skills": "Mineralogy, Geological Mapping, Earth Sciences",
        "description": "I study the Earth's structure, minerals, and geological processes.",
        "participation_tasks": "Mapping geological formations, Analyzing rock samples",
        "fields_of_science": "Geology, Earth Sciences",
    },
    {
        "name": "Lily Immunologist",
        "email": "lily.immuno@example.com",
        "username": "lilyimmuno",
        "password": "immunity123",
        "birthdate": date(1986, 12, 4),
        "skills": "Immunology, Vaccine Development, Immune Response",
        "description": "I research the immune system and work on developing vaccines.",
        "participation_tasks": "Studying immune responses, Developing vaccines",
        "fields_of_science": "Immunology, Virology",
    },
    {
        "name": "Daniel Zoologist",
        "email": "daniel.zoologist@example.com",
        "username": "danielzoo",
        "password": "wildlife123",
        "birthdate": date(1982, 8, 19),
        "skills": "Animal Behavior, Wildlife Conservation, Field Research",
        "description": "I'm fascinated by the behavior and conservation of animals.",
        "participation_tasks": "Observing animal behavior, Conducting wildlife surveys",
        "fields_of_science": "Zoology, Wildlife Biology",
    },
    {
        "name": "Grace Neuroscientist",
        "email": "grace.neuro@example.com",
        "username": "graceneuro",
        "password": "brain123",
        "birthdate": date(1987, 3, 8),
        "skills": "Neurobiology, Brain Imaging, Cognitive Neuroscience",
        "description": "I explore the mysteries of the human brain and neural processes.",
        "participation_tasks": "Brain imaging research, Studying cognitive functions",
        "fields_of_science": "Neuroscience, Cognitive Science",
    },
    {
        "name": "William Entomologist",
        "email": "william.entomo@example.com",
        "username": "williamentomo",
        "password": "insects456",
        "birthdate": date(1985, 1, 21),
        "skills": "Entomology, Insect Ecology, Taxonomy",
        "description": "I'm passionate about insects, their habitats, and their ecological roles.",
        "participation_tasks": "Collecting insect specimens, Identifying insect species",
        "fields_of_science": "Entomology, Ecology",
    },
    {
        "name": "Sophia Geneticist",
        "email": "sophia.geneticist@example.com",
        "username": "sophiagenetic",
        "password": "genetics123",
        "birthdate": date(1990, 11, 5),
        "skills": "Genetics Research, DNA Sequencing, Genetic Counseling",
        "description": "I study the genes that make us who we are and their implications.",
        "participation_tasks": "Conducting genetic research, Analyzing DNA",
        "fields_of_science": "Genetics, Molecular Biology",
    },
    {
        "name": "Lucas Archaeologist",
        "email": "lucas.archaeologist@example.com",
        "username": "lucasarcheo",
        "password": "ancientsites456",
        "birthdate": date(1983, 6, 28),
        "skills": "Archaeological Excavations, Artifact Analysis, Cultural Heritage",
        "description": "I explore ancient civilizations through archaeology and artifacts.",
        "participation_tasks": "Excavating archaeological sites, Preserving cultural heritage",
        "fields_of_science": "Archaeology, Cultural Heritage",
    },
    {
        "name": "Isabella Limnologist",
        "email": "isabella.limno@example.com",
        "username": "isabellalimno",
        "password": "water123",
        "birthdate": date(1984, 4, 15),
        "skills": "Limnology, Freshwater Ecology, Water Quality Analysis",
        "description": "I study freshwater ecosystems, their ecology, and water quality.",
        "participation_tasks": "Analyzing water quality, Studying aquatic life",
        "fields_of_science": "Limnology, Ecology",
    },
    {
        "name": "Leo Paleontologist",
        "email": "leo.paleo@example.com",
        "username": "leopaleo",
        "password": "fossils123",
        "birthdate": date(1986, 9, 9),
        "skills": "Paleontology, Fossil Excavation, Prehistoric Life",
        "description": "I uncover the secrets of prehistoric life through fossils.",
        "participation_tasks": "Excavating fossils, Identifying ancient species",
        "fields_of_science": "Paleontology, Earth History",
    }
]
