# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180825_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]
