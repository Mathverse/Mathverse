# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChicagoBoothAnalytics_app', '0020_auto_20151113_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterestedInCareerOpportunities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career_opportunities', models.ManyToManyField(related_name='userinterstedincareeropportunity_careeropportunity', to='ChicagoBoothAnalytics_app.CareerOpportunity', blank=True)),
                ('user', models.ForeignKey(related_name='userinterstedincareeropportunity_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
    ]
