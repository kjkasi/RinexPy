# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-21 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rinex', '0005_auto_20181021_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='station',
            name='lon',
        ),
        migrations.AddField(
            model_name='station',
            name='x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='station',
            name='y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='station',
            name='z',
            field=models.FloatField(default=0.0),
        ),
    ]
