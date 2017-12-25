# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_otherapplicationinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.Release')),
            ],
        ),
    ]
