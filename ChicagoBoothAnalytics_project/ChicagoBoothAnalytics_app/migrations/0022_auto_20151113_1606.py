# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChicagoBoothAnalytics_app', '0021_userinterestedincareeropportunities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinterestedincareeropportunities',
            name='career_opportunities',
        ),
        migrations.RemoveField(
            model_name='userinterestedincareeropportunities',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInterestedInCareerOpportunities',
        ),
    ]
