# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0016_careeropportunity_contact_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personorgrole',
            name='geog_regions',
            field=models.ManyToManyField(related_name='personorgrole_geog_regions', null=True, to='ChicagoBoothAnalytics_app.GeogRegion'),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='roles',
            field=models.ManyToManyField(related_name='personorgrole_roles', null=True, to='ChicagoBoothAnalytics_app.Role'),
        ),
    ]
