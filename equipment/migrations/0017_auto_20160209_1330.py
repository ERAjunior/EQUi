# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0016_auto_20160209_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name': '\u0423\u043b\u0438\u0446\u0443', 'verbose_name_plural': '\u0423\u043b\u0438\u0446\u044b'},
        ),
        migrations.AlterField(
            model_name='house',
            name='korp_house',
            field=models.CharField(blank=True, default='\u043a\u043e\u0440\u043f.', max_length=15, verbose_name='\u041a\u043e\u0440\u043f\u0443\u0441'),
        ),
    ]
