# Generated by Django 2.2.24 on 2022-06-22 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0078_add_variant_of_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeepSkyAcquisitionMigrationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deep_sky_acquisition', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='migration_records', to='astrobin.DeepSky_Acquisition')),
                ('from_gear', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='deep_sky_acquisition_migration_records_as_from', to='astrobin.Filter')),
                ('to_item', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='deep_sky_acquisition_migration_records_as_to', to='astrobin_apps_equipment.Filter')),
            ],
            options={
                'unique_together': {('deep_sky_acquisition', 'from_gear')},
            },
        ),
    ]
