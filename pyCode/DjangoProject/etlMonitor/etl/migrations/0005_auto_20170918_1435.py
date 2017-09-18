# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0004_auto_20170917_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_log',
            options={'verbose_name': '作业日志表', 'verbose_name_plural': '作业日志表'},
        ),
        migrations.AlterField(
            model_name='job_log',
            name='ACT_ED_DT',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='ACT_ED_TM',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='ACT_ST_DT',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='ACT_ST_TM',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='JOB_LG',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='RW_IST',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='RW_RD',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_log',
            name='RW_UPT',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='job_log',
            table='JOB_LOG',
        ),
    ]
