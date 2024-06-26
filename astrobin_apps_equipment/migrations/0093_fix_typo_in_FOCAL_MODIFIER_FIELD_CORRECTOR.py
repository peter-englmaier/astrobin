# Generated by Django 2.2.24 on 2022-07-15 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0092_fix_label_of_accessory_type_FIELD_DEROTATOR'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type',
            field=models.CharField(choices=[('COMPUTER', 'Computer'), ('DEW_MITIGATION', 'Dew mitigation'), ('FIELD_DEROTATOR', 'Field derotator'), ('FILTER_WHEEL', 'Filter wheel'), ('FLAT_BOX', 'Flat box'), ('FOCAL_MODIFIER_FIELD_CORRECTOR', 'Focal modifier / field corrector'), ('FOCUSER', 'Focuser'), ('OAG', 'Off-axis guider'), ('OBSERVATORY_CONTROL', 'Observatory control'), ('OBSERVATORY_DOME', 'Observatory dome'), ('POWER_DISTRIBUTION', 'Power distribution'), ('WEATHER_MONITORING', 'Weather monitoring'), ('OTHER', 'Other')], max_length=32, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='type',
            field=models.CharField(choices=[('COMPUTER', 'Computer'), ('DEW_MITIGATION', 'Dew mitigation'), ('FIELD_DEROTATOR', 'Field derotator'), ('FILTER_WHEEL', 'Filter wheel'), ('FLAT_BOX', 'Flat box'), ('FOCAL_MODIFIER_FIELD_CORRECTOR', 'Focal modifier / field corrector'), ('FOCUSER', 'Focuser'), ('OAG', 'Off-axis guider'), ('OBSERVATORY_CONTROL', 'Observatory control'), ('OBSERVATORY_DOME', 'Observatory dome'), ('POWER_DISTRIBUTION', 'Power distribution'), ('WEATHER_MONITORING', 'Weather monitoring'), ('OTHER', 'Other')], max_length=32, verbose_name='Type'),
        ),
    ]
