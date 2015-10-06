# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0006_auto_20151005_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualPersonalRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('persons', models.ManyToManyField(related_name='MutualPersonalRelationship', to='ChicagoBoothAnalytics_app.Person', blank=True)),
            ],
        ),
    ]
