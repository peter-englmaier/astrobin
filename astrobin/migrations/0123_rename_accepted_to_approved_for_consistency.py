# Generated by Django 2.2.24 on 2021-09-28 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0122_gear_migration_flag_reviewer_decision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='migration_content_type',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='contenttypes.ContentType'
            ),
        ),
        migrations.AlterField(
            model_name='gear',
            name='migration_flag_reviewer_decision',
            field=models.CharField(
                blank=True,
                choices=[
                    ('APPROVED', 'Approved'),
                    ('REJECTED_INCORRECT_STRATEGY', 'Rejected: incorrect migration strategy'),
                    ('REJECTED_WRONG_MIGRATION_TARGET', 'Rejected: wrong migration target'),
                    ('REJECTED_BAD_MIGRATION_TARGET', 'Rejected: bad migration target'),
                    ('REJECTED_OTHER', 'Rejected: other')
                ],
                max_length=32,
                null=True
            ),
        ),
    ]