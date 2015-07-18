from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as geo_models
from django.contrib.sites.models import Site
from taggit.managers import TaggableManager


class Organization(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    site = models.OneToOneField(Site)
    # allowed auths
    # google
    # twitter
    # facebook

    def __unicode__(self):
        return self.name


class Venue(geo_models.Model):
    name = models.CharField(max_length=255)
    coordinate = geo_models.PointField(null=True, blank=True)
    tags = TaggableManager()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site)

    def __unicode__(self):
        return self.name


class ExternalVenue(models.Model):
    CHOICES = (
        ('yelp', 'Yelp'),
    )

    url = models.URLField(max_length=255, unique=True,
        help_text='The canonical url for this venue on this site.')
    type = models.CharField(max_length=20, choices=CHOICES)
    venue = models.ForeignKey(Venue, related_name='references')

    def __unicode__(self):
        return '{}: {}'.format(self.get_type_display(), self.url)


class Comment(models.Model):
    CHOICES = (
        ('review', 'Review'),
    )

    type = models.CharField(max_length=20, choices=CHOICES)
    value = models.SmallIntegerField(null=True, blank=True)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    venue = models.ForeignKey(Venue)
    # user
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}: {}'.format(self.get_type_display(), self.comment[:100])
