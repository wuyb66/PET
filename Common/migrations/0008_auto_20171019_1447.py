# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-19 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_remove_globalconfiguration_releasesequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbmode',
            name='name',
            field=models.CharField(choices=[('RTDB', 'RTDB'), ('NDB', 'NDB')], default='RTDB', max_length=10),
        ),
    ]
