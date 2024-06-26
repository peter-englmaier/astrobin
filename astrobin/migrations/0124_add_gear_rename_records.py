# Generated by Django 2.2.24 on 2021-11-09 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('astrobin', '0123_rename_accepted_to_approved_for_consistency'),
    ]

    operations = [
        migrations.CreateModel(
            name='GearRenameRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('old_make', models.CharField(blank=True, max_length=128, null=True)),
                ('old_name', models.CharField(max_length=128)),
                ('new_make', models.CharField(max_length=128)),
                ('new_name', models.CharField(max_length=128)),
                ('gear', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='astrobin.Gear', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CameraRenameProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('old_make', models.CharField(blank=True, max_length=128, null=True)),
                ('old_name', models.CharField(max_length=128)),
                ('new_make', models.CharField(max_length=128)),
                ('new_name', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('AUTO_APPROVED', 'Automatically approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=13)),
                ('reject_reason', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('modified', models.BooleanField(default=False)),
                ('cooled', models.BooleanField(default=False)),
                ('sensor_make', models.CharField(blank=True, max_length=128, null=True)),
                ('sensor_name', models.CharField(blank=True, max_length=128, null=True)),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astrobin.Gear')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'gear')},
            },
        ),
    ]
