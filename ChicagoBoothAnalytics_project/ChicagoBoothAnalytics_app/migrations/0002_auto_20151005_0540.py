# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name', 'first_name_alias')},
        ),
        migrations.AddField(
            model_name='person',
            name='first_name_alias',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
