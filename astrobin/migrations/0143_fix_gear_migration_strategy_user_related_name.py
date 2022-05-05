# Generated by Django 2.2.24 on 2022-04-19 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0142_make_exposure_per_frame_decimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearmigrationstrategy',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='gear_migration_strategies',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]