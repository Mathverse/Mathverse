# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0004_facttype_orgfact_personfact'),
    ]

    operations = [
        migrations.AddField(
            model_name='personorgrole',
            name='from_when',
            field=models.DateField(null=True, verbose_name=django.db.models.fields.DateField, blank=True),
        ),
        migrations.AddField(
            model_name='personorgrole',
            name='to_when',
            field=models.DateField(null=True, verbose_name=django.db.models.fields.DateField, blank=True),
        ),
    ]
