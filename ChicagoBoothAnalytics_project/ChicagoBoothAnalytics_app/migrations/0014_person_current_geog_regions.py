# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0013_careeropportunity'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='current_geog_regions',
            field=models.ManyToManyField(related_name='person_current_geog_region', to='ChicagoBoothAnalytics_app.GeogRegion', blank=True),
        ),
    ]
