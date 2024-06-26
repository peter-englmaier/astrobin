# Generated by Django 2.2.24 on 2024-02-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0192_collection_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='bookmark_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='image',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='image',
            name='like_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
