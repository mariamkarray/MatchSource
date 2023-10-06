from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    class Meta:
        verbose_name = "CustomUser"

class ProjectCreator(CustomUser):
    projects_created = models.ManyToManyField('Project', related_name='creators', blank=True)
    class Meta:
        verbose_name = "ProjectCreator"

class Project(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(ProjectCreator, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    fields_of_science = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    project_status = models.CharField(max_length=255, null=True, blank=True)
    agency_sponsor = models.CharField(max_length=255, null=True, blank=True)
    agency_sponsor_other = models.CharField(max_length=255, null=True, blank=True)
    geographic_scope = models.CharField(max_length=255, null=True, blank=True)
    participant_age = models.CharField(max_length=255, null=True, blank=True)
    participation_tasks = models.TextField(null=True, blank=True)
    scistarter_url = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    project_url_on_catalog = models.CharField(max_length=255, null=True, blank=True)
    project_url_external = models.CharField(max_length=255, null=True, blank=True)
    cluster_id = models.IntegerField(null=True, blank=True)

class Contributer(CustomUser):
    birthdate = models.DateField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    participation_tasks = models.TextField(null=True, blank=True)
    fields_of_science = models.TextField(null=True, blank=True)
    recommended_projects = models.ManyToManyField(Project, related_name='recommended_contributers', blank=True)
    contributed_projects = models.ManyToManyField(Project, related_name='projects_contributed', blank=True)
    class Meta:
        verbose_name = "Contributer"






