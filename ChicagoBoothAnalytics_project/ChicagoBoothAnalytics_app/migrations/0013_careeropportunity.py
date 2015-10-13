# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0012_auto_20151011_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerOpportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('posting_date', models.DateField(default=django.utils.timezone.now, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('org', models.ForeignKey(related_name='careeropportunity_org', to='ChicagoBoothAnalytics_app.Org')),
                ('role', models.ForeignKey(related_name='careeropportunity_role', to='ChicagoBoothAnalytics_app.Role')),
            ],
            options={
                'ordering': ('org', 'role', '-active', '-posting_date'),
            },
        ),
    ]
