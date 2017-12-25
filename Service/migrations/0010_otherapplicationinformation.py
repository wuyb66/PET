# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0009_auto_20170616_1554'),
        ('service', '0009_auto_20170616_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherApplicationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxTrafficPerNode', models.IntegerField()),
                ('clientNumber', models.IntegerField()),
                ('minClient', models.IntegerField()),
                ('maxNodePerSystem', models.IntegerField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.ApplicationName')),
                ('hardwareModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.HardwareModel')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.Release')),
            ],
        ),
    ]
