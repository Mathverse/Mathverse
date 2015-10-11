# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0010_auto_20151011_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='level',
            field=models.ForeignKey(related_name='role_level', blank=True, to='ChicagoBoothAnalytics_app.RoleLevel', null=True),
        ),
    ]
