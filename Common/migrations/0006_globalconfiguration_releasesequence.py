# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_globalconfiguration_releasecountcpuimpact'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalconfiguration',
            name='releaseSequence',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]
