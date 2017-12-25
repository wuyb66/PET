# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20170710_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='amaRecordPerBillingBlock',
            field=models.FloatField(default=1, verbose_name='AMA Record Number per Billing Block'),
        ),
        migrations.AlterField(
            model_name='project',
            name='amaStoreDay',
            field=models.FloatField(verbose_name='AMA Store Days'),
        ),
        migrations.AlterField(
            model_name='project',
            name='averageAMARecordPerCall',
            field=models.FloatField(verbose_name='Average AMA Record per Call'),
        ),
        migrations.AlterField(
            model_name='project',
            name='clientNumber',
            field=models.IntegerField(verbose_name='Client Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cpuImpactPerRelease',
            field=models.FloatField(default=0.05, verbose_name='CPU Impact per Release'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cpuNumber',
            field=models.IntegerField(verbose_name='CPU Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cpuUsageTuning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.CPUTuning', verbose_name='CPU Usage Tuning'),
        ),
        migrations.AlterField(
            model_name='project',
            name='createTime',
            field=models.TimeField(auto_now=True, verbose_name='Create Time'),
        ),
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='database_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Common.DBMode', verbose_name='Database Type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='dbImpactPerRelease',
            field=models.FloatField(default=0.1, verbose_name='DB Impact per Release'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deploy_option',
            field=models.CharField(choices=[('individual', 'Individual'), ('combo', 'Combo')], default='combo', max_length=16, verbose_name='NDB Deploy Option'),
        ),
        migrations.AlterField(
            model_name='project',
            name='hardwareModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.HardwareModel', verbose_name='Hardware Model'),
        ),
        migrations.AlterField(
            model_name='project',
            name='memory',
            field=models.IntegerField(verbose_name='Memory'),
        ),
        migrations.AlterField(
            model_name='project',
            name='memoryImpactPerRelease',
            field=models.FloatField(default=0.1, verbose_name='Memory Impact per Release'),
        ),
        migrations.AlterField(
            model_name='project',
            name='memoryUsageTuning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.MemoryUsageTuning', verbose_name='Memory Usage Tuning'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='numberReleaseToEstimate',
            field=models.IntegerField(default=0, verbose_name='Number of Release to Estimate'),
        ),
        migrations.AlterField(
            model_name='project',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.Release', verbose_name='Release'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sigtranLinkNumber',
            field=models.IntegerField(verbose_name='SIGTRAN Link Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sigtranLinkSpeed',
            field=models.IntegerField(verbose_name='SIGTRAN Link Speed'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sigtranPortUtil',
            field=models.FloatField(verbose_name='SIGTRAN Port Utility'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='project',
            name='version',
            field=models.IntegerField(default=1, verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='project',
            name='vmType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.VMType', verbose_name='VM Type'),
        ),
    ]
