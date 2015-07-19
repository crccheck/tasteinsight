# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_organizations(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    site_model = apps.get_model('sites', 'Site')
    organization_model = apps.get_model('backend', 'Organization')
    for site in site_model.objects.all():
        organization_model.objects.get_or_create(
            site=site,
            defaults=dict(
                name=site.name,
                domain=site.domain,
            )
        )


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_organizations),
    ]
