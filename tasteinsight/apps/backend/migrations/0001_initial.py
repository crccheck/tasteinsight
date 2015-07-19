# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[('review', 'Review')])),
                ('value', models.SmallIntegerField(null=True, blank=True)),
                ('comment', models.TextField()),
                ('visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(help_text='The canonical url for this venue on this site.', unique=True, max_length=255)),
                ('type', models.CharField(max_length=20, choices=[('yelp', 'Yelp')])),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=50, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('coordinate', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(to='sites.Site')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='externalvenue',
            name='venue',
            field=models.ForeignKey(related_name='references', to='backend.Venue'),
        ),
        migrations.AddField(
            model_name='comment',
            name='venue',
            field=models.ForeignKey(to='backend.Venue'),
        ),
    ]
