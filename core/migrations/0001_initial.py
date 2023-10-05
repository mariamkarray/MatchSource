# Generated by Django 4.1.3 on 2023-10-05 22:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'CustomUser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('fields_of_science', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('project_status', models.CharField(blank=True, max_length=255, null=True)),
                ('agency_sponsor', models.CharField(blank=True, max_length=255, null=True)),
                ('agency_sponsor_other', models.CharField(blank=True, max_length=255, null=True)),
                ('geographic_scope', models.CharField(blank=True, max_length=255, null=True)),
                ('participant_age', models.CharField(blank=True, max_length=255, null=True)),
                ('project_goals', models.TextField(blank=True, null=True)),
                ('scistarter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('project_url_on_catalog', models.CharField(blank=True, max_length=255, null=True)),
                ('project_url_external', models.CharField(blank=True, max_length=255, null=True)),
                ('cluster_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCreator',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('projects_created', models.ManyToManyField(blank=True, related_name='creators', to='core.project')),
            ],
            options={
                'verbose_name': 'ProjectCreator',
            },
            bases=('core.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.projectcreator'),
        ),
        migrations.CreateModel(
            name='Contributer',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('participation_tasks', models.TextField(blank=True, null=True)),
                ('fields_of_science', models.TextField(blank=True, null=True)),
                ('contributed_projects', models.ManyToManyField(blank=True, related_name='projects_contributed', to='core.project')),
                ('recommended_projects', models.ManyToManyField(blank=True, related_name='recommended_contributers', to='core.project')),
            ],
            options={
                'verbose_name': 'Contributer',
            },
            bases=('core.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
