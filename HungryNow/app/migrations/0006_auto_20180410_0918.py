# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180409_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtemptime',
            name='Temp_wait_time',
            field=models.CharField(default='', max_length=3),
        ),
    ]