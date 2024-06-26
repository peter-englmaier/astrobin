# Generated by Django 2.2.24 on 2021-10-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0113_add_gearuserinfo_modded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_gallery_sorting',
            field=models.SmallIntegerField(choices=[(0, 'Publication'), (1, 'Acquisition'), (2, 'Subject type'), (3, 'Year'), (4, 'Gear'), (5, 'Collections'), (6, 'Title'), (7, 'Constellation')], default=0, verbose_name='Default gallery sorting'),
        ),
    ]
