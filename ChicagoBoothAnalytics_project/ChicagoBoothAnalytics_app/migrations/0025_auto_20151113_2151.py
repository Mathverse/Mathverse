# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0024_usercareeropportunitystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerOpportunityURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ('url',),
            },
        ),
        migrations.AddField(
            model_name='careeropportunity',
            name='urls',
            field=models.ManyToManyField(related_name='careeropportunity_urls', to='ChicagoBoothAnalytics_app.CareerOpportunityURL', blank=True),
        ),
    ]
