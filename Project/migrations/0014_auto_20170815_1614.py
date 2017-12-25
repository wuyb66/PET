# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0010_auto_20170623_1125'),
        ('project', '0013_auto_20170710_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpuNumber', models.IntegerField(choices=[(2, '2 Cores'), (4, '4 Cores'), (6, '6 Cores'), (8, '8 Cores'), (10, '10 Cores'), (12, '12 Cores'), (14, '14 Cores'), (16, '16 Cores'), (18, '18 Cores'), (20, '20 Cores'), (22, '22 Cores'), (24, '24 Cores'), (26, '26 Cores'), (28, '28 Cores'), (30, '30 Cores'), (32, '32 Cores'), (34, '34 Cores'), (36, '36 Cores'), (38, '38 Cores'), (40, '40 Cores'), (42, '42 Cores'), (44, '44 Cores'), (46, '46 Cores')], verbose_name='CPU Number')),
                ('memory', models.IntegerField(verbose_name='Memory')),
                ('clientNumber', models.IntegerField(verbose_name='Client Number')),
                ('sigtranLinkSpeed', models.IntegerField(verbose_name='SIGTRAN Link Speed')),
                ('sigtranLinkNumber', models.IntegerField(verbose_name='SIGTRAN Link Number')),
                ('sigtranPortUtil', models.FloatField(verbose_name='SIGTRAN Port Utility')),
                ('amaRecordPerBillingBlock', models.FloatField(default=1, verbose_name='AMA Record Number per Billing Block')),
                ('numberReleaseToEstimate', models.IntegerField(default=0, verbose_name='Number of Release to Estimate')),
                ('cpuImpactPerRelease', models.FloatField(default=0.05, verbose_name='CPU Impact per Release')),
                ('memoryImpactPerRelease', models.FloatField(default=0.1, verbose_name='Memory Impact per Release')),
                ('dbImpactPerRelease', models.FloatField(default=0.1, verbose_name='DB Impact per Release')),
                ('deploy_option', models.CharField(choices=[('individual', 'Individual'), ('combo', 'Combo')], default='combo', max_length=16, verbose_name='NDB Deploy Option')),
                ('averageAMARecordPerCall', models.FloatField(verbose_name='Average AMA Record per Call')),
                ('amaStoreDay', models.FloatField(verbose_name='AMA Store Days')),
                ('activeSubscriber', models.IntegerField(verbose_name='Active Subscriber')),
                ('inactiveSubscriber', models.IntegerField(verbose_name='Inactive Subscriber')),
                ('groupAccountNumber', models.IntegerField(verbose_name='Number of Group Account')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.CPU')),
                ('cpuUsageTuning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.CPUTuning', verbose_name='CPU Usage Tuning')),
                ('memoryUsageTuning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.MemoryUsageTuning', verbose_name='Memory Usage Tuning')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='activeSubscriber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='amaRecordPerBillingBlock',
        ),
        migrations.RemoveField(
            model_name='project',
            name='amaStoreDay',
        ),
        migrations.RemoveField(
            model_name='project',
            name='averageAMARecordPerCall',
        ),
        migrations.RemoveField(
            model_name='project',
            name='clientNumber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cpuImpactPerRelease',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cpuNumber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cpuUsageTuning',
        ),
        migrations.RemoveField(
            model_name='project',
            name='dbImpactPerRelease',
        ),
        migrations.RemoveField(
            model_name='project',
            name='deploy_option',
        ),
        migrations.RemoveField(
            model_name='project',
            name='groupAccountNumber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='hardwareModel',
        ),
        migrations.RemoveField(
            model_name='project',
            name='inactiveSubscriber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='project',
            name='memoryImpactPerRelease',
        ),
        migrations.RemoveField(
            model_name='project',
            name='memoryUsageTuning',
        ),
        migrations.RemoveField(
            model_name='project',
            name='numberReleaseToEstimate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sigtranLinkNumber',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sigtranLinkSpeed',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sigtranPortUtil',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vmType',
        ),
        migrations.AddField(
            model_name='project',
            name='hardwareType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hardware.HardwareType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='projectinformation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Project'),
        ),
        migrations.AddField(
            model_name='projectinformation',
            name='vmType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.VMType', verbose_name='VM Type'),
        ),
    ]
