# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0003_org_personorgrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('label',),
            },
        ),
        migrations.CreateModel(
            name='OrgFact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fact', models.CharField(max_length=255)),
                ('fact_type', models.ForeignKey(related_name='OrgFact', to='ChicagoBoothAnalytics_app.FactType')),
                ('org', models.ForeignKey(related_name='OrgFact', to='ChicagoBoothAnalytics_app.Org')),
            ],
            options={
                'ordering': ('org', 'fact_type', 'fact'),
            },
        ),
        migrations.CreateModel(
            name='PersonFact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fact', models.CharField(max_length=255)),
                ('fact_type', models.ForeignKey(related_name='PersonFact', to='ChicagoBoothAnalytics_app.FactType')),
                ('person', models.ForeignKey(related_name='PersonFact', to='ChicagoBoothAnalytics_app.Person')),
            ],
            options={
                'ordering': ('person', 'fact_type', 'fact'),
            },
        ),
    ]
