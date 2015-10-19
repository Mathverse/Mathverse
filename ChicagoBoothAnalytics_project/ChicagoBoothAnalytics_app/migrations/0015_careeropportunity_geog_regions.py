# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0014_person_current_geog_regions'),
    ]

    operations = [
        migrations.AddField(
            model_name='careeropportunity',
            name='geog_regions',
            field=models.ManyToManyField(related_name='careeropportunity_geog_regions', to='ChicagoBoothAnalytics_app.GeogRegion', blank=True),
        ),
    ]
