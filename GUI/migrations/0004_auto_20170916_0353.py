# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0003_defense_node_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attack_node',
            name='id',
        ),
        migrations.AlterField(
            model_name='attack_node',
            name='name',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
