# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_auto_20140907_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='completed_on',
            field=models.DateField(null=True, blank=True),
        ),
    ]
