# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0019_auto_20151105_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='careeropportunity',
            options={'ordering': ('org', 'role', '-open', '-posting_date')},
        ),
        migrations.RenameField(
            model_name='careeropportunity',
            old_name='active',
            new_name='open',
        ),
    ]
