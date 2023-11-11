# Generated by Django 2.2.24 on 2023-11-10 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_iotd', '0019_fix_relationship_to_user_in_iotdstaffmemberscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='active_days',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='period_end',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 31, 23, 59, 59)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='period_start',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='promotions_dismissals_accuracy_ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
