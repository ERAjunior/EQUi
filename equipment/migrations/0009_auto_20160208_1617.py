# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0008_house_num_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='korp_house',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]