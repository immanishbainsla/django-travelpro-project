# Generated by Django 2.2.3 on 2019-08-29 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField(help_text='Describe your Query here.')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='accounts/profile_pics')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('current_address', models.TextField(help_text='Enter your Home Address Here.')),
                ('parmanent_address', models.TextField(blank=True, help_text='Enter Where are you travelling?', null=True)),
                ('travel_reason', models.CharField(blank=True, help_text='eg. Solo Trip!', max_length=100, null=True)),
                ('age', models.PositiveIntegerField(default=20)),
                ('portfolio_site', models.URLField(blank=True, default='https://www.example.com')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-slug'],
            },
        ),
    ]
