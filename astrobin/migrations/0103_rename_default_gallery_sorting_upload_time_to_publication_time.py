# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-10 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0102_add_constellation_to_default_gallery_sorting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_gallery_sorting',
            field=models.SmallIntegerField(
                choices=[(0, 'Publication time'), (1, 'Acquisition time'), (2, 'Subject type'), (3, 'Year'),
                         (4, 'Gear'), (5, 'Collections'), (6, 'Title'), (7, 'Constellation')], default=0,
                verbose_name='Default gallery sorting'),
        ),
    ]