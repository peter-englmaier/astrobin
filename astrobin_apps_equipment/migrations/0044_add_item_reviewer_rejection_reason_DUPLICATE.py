# Generated by Django 2.2.24 on 2022-04-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0043_equipmentpreset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='camera',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='filter',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='mount',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[
                    ('TYPO', "There's a typo in the name of the item"),
                    ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                    ('INACCURATE_DATA', 'Some data is inaccurate'),
                    ('INSUFFICIENT_DATA', 'Some important data is missing'),
                    ('DUPLICATE', 'This item already exists in the database'),
                    ('OTHER', 'Other')
                ],
                editable=False,
                max_length=32,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='software',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='reviewer_rejection_reason',
            field=models.CharField(
                choices=[('TYPO', "There's a typo in the name of the item"),
                         ('WRONG_BRAND', 'The item was assigned to the wrong brand'),
                         ('INACCURATE_DATA', 'Some data is inaccurate'),
                         ('INSUFFICIENT_DATA', 'Some important data is missing'),
                         ('DUPLICATE', 'This item already exists in the database'), ('OTHER', 'Other')], editable=False,
                max_length=32, null=True
            ),
        ),
    ]