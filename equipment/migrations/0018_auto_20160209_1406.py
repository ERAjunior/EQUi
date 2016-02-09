# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0017_auto_20160209_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwitchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')),
                ('num_ports_model', models.IntegerField(default=1, verbose_name='\u041a\u043e\u043b-\u0432\u043e (\u043c\u0435\u0434\u043d\u044b\u0445) \u043f\u043e\u0440\u0442\u043e\u0432')),
                ('num_watt_model', models.IntegerField(default=1, verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0435\u043c\u0430\u044f \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0432 \u0412\u0442')),
                ('date_create_model', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'switch_model',
                'verbose_name': '\u041c\u043e\u0434\u0435\u043b\u044c',
                'verbose_name_plural': '\u041c\u043e\u0434\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='VendorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200, verbose_name='\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c')),
                ('date_create_vendor', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vendor_model',
                'verbose_name': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.AddField(
            model_name='switchmodel',
            name='vendor_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.VendorModel'),
        ),
    ]
