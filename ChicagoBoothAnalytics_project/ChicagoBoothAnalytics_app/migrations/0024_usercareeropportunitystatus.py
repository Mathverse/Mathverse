# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChicagoBoothAnalytics_app', '0023_userinterestedinorgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCareerOpportunityStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=300)),
                ('career_opportunity', models.ForeignKey(related_name='usercareeropportunity_career_opportunity', to='ChicagoBoothAnalytics_app.CareerOpportunity')),
                ('user', models.ForeignKey(related_name='usercareeropportunity_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user', 'career_opportunity'),
            },
        ),
    ]
