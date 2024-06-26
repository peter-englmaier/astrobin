# Generated by Django 2.2.24 on 2023-11-06 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('astrobin_apps_iotd', '0015_iotdsubmitterseenimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='IotdStaffMemberScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('promoted_images', models.PositiveIntegerField(default=0)),
                ('promoted_images_to_tpn', models.PositiveIntegerField(default=0)),
                ('promoted_images_to_tp', models.PositiveIntegerField(default=0)),
                ('promoted_images_to_iotd', models.PositiveIntegerField(default=0)),
                ('dismissed_images', models.PositiveIntegerField(default=0)),
                ('correct_dismissals', models.PositiveIntegerField(default=0)),
                ('dismissed_images_to_tpn', models.PositiveIntegerField(default=0)),
                ('dismissed_images_to_tp', models.PositiveIntegerField(default=0)),
                ('dismissed_images_to_iotd', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='iotd_staff_member_score', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-score',),
            },
        ),
    ]
