from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

class ProjectCreator(AbstractUser):
    pass


class Project(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(ProjectCreator, on_delete=models.CASCADE, related_name='projects')

class FieldOfScience(models.Model):
    name = models.CharField(max_length=255)

class Contributer(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    participation_tasks = models.ManyToManyField('Project', blank=True)
    fields_of_science = models.ManyToManyField('FieldOfScience', blank=True)

class ContributedProject(models.Model):
    user = models.ForeignKey(Contributer, on_delete=models.CASCADE, related_name='contributed_projects')
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

class RecommendedProject(models.Model):
    user = models.ForeignKey(Contributer, on_delete=models.CASCADE, related_name='recommended_projects')
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    confidence_level = models.PositiveIntegerField()

class SimilarUser(models.Model):
    user = models.ForeignKey(Contributer, on_delete=models.CASCADE, related_name='similar_users')
    similar_user = models.ForeignKey(Contributer, on_delete=models.CASCADE)
    confidence_level = models.PositiveIntegerField()

class ProjectCreator(AbstractUser):
    user = models.OneToOneField(Contributer, on_delete=models.CASCADE, primary_key=True)
    projects_created = models.ManyToManyField('Project', related_name='creators', blank=True)
