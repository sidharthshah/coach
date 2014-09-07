# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('difficulty', models.IntegerField(default=1, choices=[(1, b'Easy'), (2, b'Intermediate'), (3, b'Difficult'), (4, b'Epic')])),
                ('details', models.TextField(default=b'', null=True, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Pending'), (2, b'Doing'), (3, b'Completed'), (4, b'Differed')])),
                ('link_to_material', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProblemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProblemSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('difficulty', models.IntegerField(default=1, choices=[(1, b'Easy'), (2, b'Intermediate'), (3, b'Difficult'), (4, b'Epic')])),
                ('details', models.TextField(default=b'', null=True, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Pending'), (2, b'Doing'), (3, b'Completed'), (4, b'Differed')])),
                ('link_to_material', models.URLField()),
                ('category', models.ForeignKey(to='trainings.ProblemCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='problem',
            name='category',
            field=models.ForeignKey(to='trainings.ProblemCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problem',
            name='source',
            field=models.ForeignKey(to='trainings.ProblemSource'),
            preserve_default=True,
        ),
    ]
