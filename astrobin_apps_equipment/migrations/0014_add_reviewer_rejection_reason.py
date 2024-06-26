# Generated by Django 2.2.24 on 2021-09-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0013_add_review_fields_to_equipment_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='reviewer_rejection_reason',
            field=models.CharField(choices=[('TYPO', "There's a typo in the name of the item"), ('WRONG_BRAND', 'The item was assigned to the wrong brand'), ('INACCURATE_DATA', 'Some data is inaccurate'), ('INSUFFICIENT_DATA', 'Some important data is missing'), ('OTHER', 'Other')], editable=False, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='reviewer_rejection_reason',
            field=models.CharField(choices=[('TYPO', "There's a typo in the name of the item"), ('WRONG_BRAND', 'The item was assigned to the wrong brand'), ('INACCURATE_DATA', 'Some data is inaccurate'), ('INSUFFICIENT_DATA', 'Some important data is missing'), ('OTHER', 'Other')], editable=False, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='telescope',
            name='reviewer_rejection_reason',
            field=models.CharField(choices=[('TYPO', "There's a typo in the name of the item"), ('WRONG_BRAND', 'The item was assigned to the wrong brand'), ('INACCURATE_DATA', 'Some data is inaccurate'), ('INSUFFICIENT_DATA', 'Some important data is missing'), ('OTHER', 'Other')], editable=False, max_length=32, null=True),
        ),
    ]
