# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_street'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='date_up_area',
            new_name='date_create_area',
        ),
        migrations.RenameField(
            model_name='street',
            old_name='date_up_street',
            new_name='date_create_street',
        ),
    ]
