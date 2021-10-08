# Generated by Django 2.2.24 on 2021-09-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_platesolving', '0020_update_some_solution_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlateSolvingAdvancedLiveLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(editable=False, max_length=32)),
                ('timestamp', models.DateTimeField(editable=False)),
                ('stage', models.CharField(editable=False, max_length=32)),
                ('log', models.TextField(null=True, editable=False)),
            ],
        ),
    ]