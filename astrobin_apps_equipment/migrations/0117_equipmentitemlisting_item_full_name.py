# Generated by Django 2.2.24 on 2024-01-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0116_add_equipment_item_thumbnail_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentitemlisting',
            name='item_full_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
