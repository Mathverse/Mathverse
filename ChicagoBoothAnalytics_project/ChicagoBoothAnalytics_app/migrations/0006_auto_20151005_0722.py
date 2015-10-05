# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0005_auto_20151005_0713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personorgrole',
            options={'ordering': ('person', 'org', 'to_when', 'role')},
        ),
    ]
