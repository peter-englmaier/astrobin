# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-07 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0106_add_image_full_size_display_limitations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='timezone',
        ),
    ]
