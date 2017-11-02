# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 01:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maternity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('quality', models.IntegerField()),
                ('frequency', models.CharField(max_length=200)),
                ('health', models.CharField(max_length=200)),
                ('nicu', models.BooleanField()),
                ('reason', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='maternity',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Patient'),
        ),
    ]
