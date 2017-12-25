# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-29 08:17
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0011_hardwaretype_cpus'),
        ('project', '0018_auto_20170915_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='hardwareType',
        ),
        migrations.AddField(
            model_name='project',
            name='hardwareType',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='cpu', chained_model_field='cpus', to='Hardware.HardwareModel'),
        ),
    ]
