# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rtemptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtemptime',
            name='temp_date',
            field=models.CharField(default='Not Entered', max_length=50),
        ),
        migrations.AlterField(
            model_name='rtemptime',
            name='Temp_wait_time',
            field=models.CharField(default='Not Entered', max_length=50),
        ),
    ]
