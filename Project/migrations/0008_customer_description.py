# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_auto_20170705_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
