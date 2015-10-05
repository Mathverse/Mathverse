# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0002_auto_20151005_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PersonOrgRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=255)),
                ('org', models.ForeignKey(related_name='PersonOrgRole', to='ChicagoBoothAnalytics_app.Org')),
                ('person', models.ForeignKey(related_name='PersonOrgRole', to='ChicagoBoothAnalytics_app.Person')),
            ],
            options={
                'ordering': ('person', 'org', 'role'),
            },
        ),
    ]
