# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0002_auto_20170916_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB_LOG',
            fields=[
                ('JOB_SEQ_ID', models.AutoField(primary_key=True, serialize=False)),
                ('JOB_STS', models.CharField(max_length=12)),
                ('JOB_NM', models.CharField(max_length=128)),
                ('DATA_PRD', models.CharField(max_length=10)),
                ('ACT_ST_DT', models.DateField()),
                ('ACT_ST_TM', models.TimeField()),
                ('ACT_ED_DT', models.DateField()),
                ('ACT_ED_TM', models.TimeField()),
                ('JOB_LG', models.CharField(max_length=24)),
                ('RW_RD', models.IntegerField()),
                ('RW_IST', models.IntegerField()),
                ('RW_UPT', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JOB_METADATA',
            fields=[
                ('JOB_ID', models.AutoField(primary_key=True, serialize=False)),
                ('JOB_NM', models.CharField(max_length=128)),
                ('SCHD_PERIOD', models.CharField(max_length=12)),
                ('JOB_TP', models.CharField(max_length=15)),
                ('LOCATION', models.CharField(max_length=255)),
                ('JOBCMD', models.CharField(max_length=255)),
                ('PARAMS', models.CharField(max_length=255)),
                ('PRIORITY', models.CharField(max_length=255)),
                ('EST_WRKLD', models.CharField(max_length=255)),
                ('PLD_ST_DT', models.DateField()),
                ('PLD_ST_TM', models.TimeField()),
                ('EXP_ED_DT', models.DateField()),
                ('EXP_ED_TM', models.TimeField()),
                ('MTX_GRP', models.CharField(max_length=128)),
                ('NTY_PTY', models.CharField(max_length=128)),
                ('INIT_FLAG', models.CharField(max_length=2)),
                ('PPN_TSTMP', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='JOB_SEQ',
            fields=[
                ('SEQ_ID', models.AutoField(primary_key=True, serialize=False)),
                ('JOB_NM', models.CharField(max_length=128)),
                ('PRE_JOB', models.CharField(max_length=128)),
                ('SEQ_TY', models.CharField(max_length=128)),
            ],
        ),
    ]