# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0009_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='PHONE',
            new_name='MOBILE',
        ),
    ]
