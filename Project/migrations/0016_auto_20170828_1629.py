# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-28 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20170822_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinformation',
            name='cpuNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.CPUList', verbose_name='CPU Number'),
        ),
    ]
