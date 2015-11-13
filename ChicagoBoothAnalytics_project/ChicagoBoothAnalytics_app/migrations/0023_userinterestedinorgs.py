# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChicagoBoothAnalytics_app', '0022_auto_20151113_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterestedInOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgs', models.ManyToManyField(related_name='userinterstedinorgs_orgs', to='ChicagoBoothAnalytics_app.Org', blank=True)),
                ('user', models.ForeignKey(related_name='userinterstedinorgs_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
    ]
