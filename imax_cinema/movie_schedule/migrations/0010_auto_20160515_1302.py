# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0009_auto_20160515_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket',
            new_name='seats',
        ),
    ]
