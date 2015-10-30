# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0017_auto_20151030_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personorgrole',
            name='geog_regions',
            field=models.ManyToManyField(related_name='personorgrole_geog_regions', to='ChicagoBoothAnalytics_app.GeogRegion', blank=True),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='roles',
            field=models.ManyToManyField(related_name='personorgrole_roles', to='ChicagoBoothAnalytics_app.Role', blank=True),
        ),
    ]
