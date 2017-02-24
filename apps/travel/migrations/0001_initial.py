# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelers_user', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=90)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_user', to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='travelers',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelers_trip', to='travel.Trips'),
        ),
    ]