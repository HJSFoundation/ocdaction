# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-15 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_split_up_tasks_separate_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_compulsions',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='task',
            name='task_fears',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='task',
            name='task_goals',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
