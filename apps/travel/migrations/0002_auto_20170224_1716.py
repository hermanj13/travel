# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='start',
            field=models.DateField(),
        ),
    ]
