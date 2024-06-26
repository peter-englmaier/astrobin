# Generated by Django 2.2.24 on 2022-04-29 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0143_fix_gear_migration_strategy_user_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appapikeyrequest',
            name='description',
            field=models.TextField(
                default='n/a',
                help_text='Please explain the purpose of your application, and how you intend to use the API.',
                validators=[
                    django.core.validators.MinLengthValidator(100),
                    django.core.validators.MaxLengthValidator(500)
                ],
                verbose_name='Description'
            ),
            preserve_default=False,
        ),
    ]
