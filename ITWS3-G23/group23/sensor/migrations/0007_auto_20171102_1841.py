# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_auto_20171101_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_id', models.IntegerField()),
                ('latitude', models.CharField(max_length=250)),
                ('longitude', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='sensor_read',
            name='plant_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sensor.plant'),
        ),
    ]
