# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0008_auto_20170616_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cputuning',
            old_name='cpuUsageTuning',
            new_name='clientCPUUsage',
        ),
        migrations.AddField(
            model_name='cputuning',
            name='systemCPUUsage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
