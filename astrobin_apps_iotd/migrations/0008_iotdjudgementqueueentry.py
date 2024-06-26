# Generated by Django 2.2.24 on 2021-12-17 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('astrobin_apps_iotd', '0007_iotdstaffmembersettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='IotdJudgementQueueEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_vote_timestamp', models.DateTimeField()),
                ('image', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='judgement_queue_entry',
                    to='astrobin.Image'
                )),
                ('judge', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='judgement_queue_entry',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'ordering': ('last_vote_timestamp',),
                'unique_together': {('judge', 'image')},
            },
        ),
    ]
