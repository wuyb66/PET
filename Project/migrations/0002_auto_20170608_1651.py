# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='database_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Common.DBMode'),
        ),
    ]
