# Generated by Django 2.2.24 on 2022-07-18 07:09

from django.db import migrations, models


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
        ('astrobin_apps_equipment', '0094_convert_equipment_user_and_image_count_from_null_to_zero'),
    ]

    operations = [
        migrations.RunPython(
            make_null_values_zeros,
            revert_make_null_values_zeros
        ),
        migrations.AlterField(
            model_name='accessory',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='camera',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='camera',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='filter',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='filter',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='mount',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='mount',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='software',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='software',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='user_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        )
    ]
