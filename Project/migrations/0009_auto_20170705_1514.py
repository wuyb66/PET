# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0008_customer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
