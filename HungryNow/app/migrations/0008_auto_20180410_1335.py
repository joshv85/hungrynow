# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180410_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtemptime',
            name='Temp_wait_time',
            field=models.IntegerField(),
        ),
    ]
