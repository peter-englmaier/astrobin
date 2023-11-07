# Generated by Django 2.2.24 on 2023-11-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_iotd', '0016_iotdstaffmemberscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='dismissed_images',
            new_name='dismissals',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='dismissed_images_to_iotd',
            new_name='dismissals_to_iotd',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='dismissed_images_to_tp',
            new_name='dismissals_to_tp',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='dismissed_images_to_tpn',
            new_name='dismissals_to_tpn',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='promoted_images',
            new_name='promotions',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='promoted_images_to_iotd',
            new_name='promotions_to_iotd',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='promoted_images_to_tp',
            new_name='promotions_to_tp',
        ),
        migrations.RenameField(
            model_name='iotdstaffmemberscore',
            old_name='promoted_images_to_tpn',
            new_name='promotions_to_tpn',
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='missed_dismissals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='missed_iotd_promotions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='missed_tp_promotions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='missed_tpn_promotions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iotdstaffmemberscore',
            name='wasted_promotion',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
