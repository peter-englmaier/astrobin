# Generated by Django 2.2.24 on 2022-06-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0150_add_submitted_for_iotd_tp_consideration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='key',
            field=models.CharField(blank=True, default='', editable=False, max_length=256),
        ),
    ]
