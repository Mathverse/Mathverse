# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0015_careeropportunity_geog_regions'),
    ]

    operations = [
        migrations.AddField(
            model_name='careeropportunity',
            name='contact_persons',
            field=models.ManyToManyField(related_name='careeropportunity_contact_persons', to='ChicagoBoothAnalytics_app.Person', blank=True),
        ),
    ]
