# Generated by Django 2.2.24 on 2021-11-17 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0039_software_softwareeditproposal'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('klass', models.CharField(choices=[('SENSOR', 'Sensor'), ('CAMERA', 'Camera'), ('TELESCOPE', 'Telescope'), ('MOUNT', 'Mount'), ('FILTER', 'Filter'), ('ACCESSORY', 'Accessory'), ('SOFTWARE', 'Software')], max_length=16, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='accessory',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='accessoryeditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='camera',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='cameraeditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='filter',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='filtereditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='mount',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='mounteditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='sensoreditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='software',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='softwareeditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='telescope',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
        migrations.AddField(
            model_name='telescopeeditproposal',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='astrobin_apps_equipment.EquipmentItemGroup'),
        ),
    ]
