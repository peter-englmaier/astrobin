# Generated by Django 2.2.24 on 2022-07-18 07:09

from django.db import migrations


def make_null_values_zeros(apps, schema_editor):
    for ModelClass in (
            apps.get_model('astrobin_apps_equipment', 'Sensor'),
            apps.get_model('astrobin_apps_equipment', 'SensorEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Camera'),
            apps.get_model('astrobin_apps_equipment', 'CameraEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Telescope'),
            apps.get_model('astrobin_apps_equipment', 'TelescopeEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Mount'),
            apps.get_model('astrobin_apps_equipment', 'MountEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Filter'),
            apps.get_model('astrobin_apps_equipment', 'FilterEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Accessory'),
            apps.get_model('astrobin_apps_equipment', 'AccessoryEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Software'),
            apps.get_model('astrobin_apps_equipment', 'SoftwareEditProposal'),
    ):
        ModelClass.objects.filter(user_count__isnull=True).update(user_count=0)
        ModelClass.objects.filter(image_count__isnull=True).update(image_count=0)


def revert_make_null_values_zeros(apps, schema_editor):
    for ModelClass in (
            apps.get_model('astrobin_apps_equipment', 'Sensor'),
            apps.get_model('astrobin_apps_equipment', 'SensorEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Camera'),
            apps.get_model('astrobin_apps_equipment', 'CameraEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Telescope'),
            apps.get_model('astrobin_apps_equipment', 'TelescopeEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Mount'),
            apps.get_model('astrobin_apps_equipment', 'MountEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Filter'),
            apps.get_model('astrobin_apps_equipment', 'FilterEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Accessory'),
            apps.get_model('astrobin_apps_equipment', 'AccessoryEditProposal'),
            apps.get_model('astrobin_apps_equipment', 'Software'),
            apps.get_model('astrobin_apps_equipment', 'SoftwareEditProposal'),
    ):
        ModelClass.objects.filter(user_count=0).update(user_count=None)
        ModelClass.objects.filter(image_count=0).update(image_count=None)


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0093_fix_typo_in_FOCAL_MODIFIER_FIELD_CORRECTOR'),
    ]

    operations = [
        migrations.RunPython(
            make_null_values_zeros,
            revert_make_null_values_zeros
        ),
    ]
