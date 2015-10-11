# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0009_auto_20151010_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='business_sectors',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.BusinessSector', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='geog_regions',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.GeogRegion', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='roles',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.Role', blank=True),
        ),
    ]
