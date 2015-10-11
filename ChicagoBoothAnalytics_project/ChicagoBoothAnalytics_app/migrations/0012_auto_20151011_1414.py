# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0011_auto_20151011_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutualpersonalrelationship',
            name='persons',
            field=models.ManyToManyField(related_name='mutualpersonalrelationship_persons', to='ChicagoBoothAnalytics_app.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='business_sectors',
            field=models.ManyToManyField(related_name='org_business_sectors', to='ChicagoBoothAnalytics_app.BusinessSector', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='geog_regions',
            field=models.ManyToManyField(related_name='org_geog_regions', to='ChicagoBoothAnalytics_app.GeogRegion', blank=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='roles',
            field=models.ManyToManyField(related_name='org_roles', to='ChicagoBoothAnalytics_app.Role', blank=True),
        ),
        migrations.AlterField(
            model_name='orgfact',
            name='fact_type',
            field=models.ForeignKey(related_name='orgfact_type', to='ChicagoBoothAnalytics_app.FactType'),
        ),
        migrations.AlterField(
            model_name='orgfact',
            name='org',
            field=models.ForeignKey(related_name='orgfact_org', to='ChicagoBoothAnalytics_app.Org'),
        ),
        migrations.AlterField(
            model_name='personfact',
            name='fact_type',
            field=models.ForeignKey(related_name='personfact_type', to='ChicagoBoothAnalytics_app.FactType'),
        ),
        migrations.AlterField(
            model_name='personfact',
            name='person',
            field=models.ForeignKey(related_name='personfact_person', to='ChicagoBoothAnalytics_app.Person'),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='geog_regions',
            field=models.ManyToManyField(related_name='personorgrole_geog_regions', to='ChicagoBoothAnalytics_app.GeogRegion'),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='org',
            field=models.ForeignKey(related_name='personorgrole_org', to='ChicagoBoothAnalytics_app.Org'),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='person',
            field=models.ForeignKey(related_name='personorgrole_person', to='ChicagoBoothAnalytics_app.Person'),
        ),
        migrations.AlterField(
            model_name='personorgrole',
            name='roles',
            field=models.ManyToManyField(related_name='personorgrole_roles', to='ChicagoBoothAnalytics_app.Role'),
        ),
    ]
