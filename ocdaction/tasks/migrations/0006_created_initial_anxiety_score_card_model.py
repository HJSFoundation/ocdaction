# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-16 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_created_initial_anxiety_score_model_rename_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnxietyScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_after_10_min', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_10', to='tasks.AnxietyScore')),
                ('score_after_15_min', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_15', to='tasks.AnxietyScore')),
                ('score_after_20_min', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_20', to='tasks.AnxietyScore')),
                ('score_after_5_min', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_5', to='tasks.AnxietyScore')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
        ),
    ]