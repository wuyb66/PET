# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-22 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0013_auto_20171122_1438'),
        ('Project', '0031_auto_20171122_1438'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='featureconfiguration',
            unique_together=set([('project', 'feature')]),
        ),
    ]
