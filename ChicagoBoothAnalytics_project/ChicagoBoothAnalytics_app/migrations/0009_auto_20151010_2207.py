# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0008_auto_20151011_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='level',
            field=models.ForeignKey(related_name='Role', blank=True, to='ChicagoBoothAnalytics_app.RoleLevel', null=True),
        ),
    ]
