# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0028_switch_pd_switch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='pd_switch',
            field=models.CharField(blank=True, default='\u043f\u0434.', max_length=100, null=True),
        ),
    ]
