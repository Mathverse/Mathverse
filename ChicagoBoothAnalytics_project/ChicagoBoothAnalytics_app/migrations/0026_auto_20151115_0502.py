# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0025_auto_20151113_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careeropportunity',
            name='url',
        ),
        migrations.RemoveField(
            model_name='org',
            name='roles',
        ),
    ]
