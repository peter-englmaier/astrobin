# Generated by Django 2.2.24 on 2024-02-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0196_image_final_gallery_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]