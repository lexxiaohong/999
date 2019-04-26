# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
    ]
