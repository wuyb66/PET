# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-17 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20171117_1433'),
        ('project', '0029_auto_20171110_1638'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trafficinformation',
            unique_together=set([('project', 'callType')]),
        ),
        migrations.AlterModelTable(
            name='trafficinformation',
            table='Traffic Information',
        ),
    ]
