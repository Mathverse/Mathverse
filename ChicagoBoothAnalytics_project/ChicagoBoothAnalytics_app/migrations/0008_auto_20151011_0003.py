# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0007_mutualpersonalrelationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GeogRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('level', 'title'),
            },
        ),
        migrations.CreateModel(
            name='RoleLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=255)),
                ('level_number_from_high_to_low', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('level_number_from_high_to_low',),
            },
        ),
        migrations.AlterModelOptions(
            name='personorgrole',
            options={'ordering': ('person', 'org', 'to_when')},
        ),
        migrations.RemoveField(
            model_name='personorgrole',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='level',
            field=models.ForeignKey(related_name='Role', to='ChicagoBoothAnalytics_app.RoleLevel'),
        ),
        migrations.AddField(
            model_name='org',
            name='business_sectors',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.BusinessSector'),
        ),
        migrations.AddField(
            model_name='org',
            name='geog_regions',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.GeogRegion'),
        ),
        migrations.AddField(
            model_name='org',
            name='roles',
            field=models.ManyToManyField(related_name='Org', to='ChicagoBoothAnalytics_app.Role'),
        ),
        migrations.AddField(
            model_name='personorgrole',
            name='geog_regions',
            field=models.ManyToManyField(related_name='PersonOrgRole', to='ChicagoBoothAnalytics_app.GeogRegion'),
        ),
        migrations.AddField(
            model_name='personorgrole',
            name='roles',
            field=models.ManyToManyField(related_name='PersonOrgRole', to='ChicagoBoothAnalytics_app.Role'),
        ),
    ]
