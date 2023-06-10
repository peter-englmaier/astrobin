# Generated by Django 2.2.24 on 2023-05-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0170_add_maksutov_newtonian_telescope_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarsystem_acquisition',
            name='gain',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Gain'),
        ),
        migrations.AddField(
            model_name='solarsystem_acquisition',
            name='iso',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ISO'),
        ),
        migrations.AlterField(
            model_name='deepsky_acquisition',
            name='flat_darks',
            field=models.PositiveIntegerField(blank=True, help_text='The number of flat dark frames.', null=True, verbose_name='Flat darks'),
        ),
    ]