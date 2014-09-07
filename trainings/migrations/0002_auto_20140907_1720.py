# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('completed_on', models.DateField()),
                ('comments', models.TextField(null=True, blank=True)),
                ('problem_1', models.ForeignKey(related_name=b'Problem 1', to='trainings.Problem')),
                ('problem_2', models.ForeignKey(related_name=b'Problem 2', blank=True, to='trainings.Problem', null=True)),
                ('problem_3', models.ForeignKey(related_name=b'Problem 3', blank=True, to='trainings.Problem', null=True)),
                ('tutorial', models.ForeignKey(to='trainings.Tutorial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='problemcategory',
            options={'verbose_name_plural': 'Problem Categories'},
        ),
    ]
