# Generated by Django 2.2.24 on 2021-09-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_platesolving', '0019_update_some_platesolving_settings_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='solutions'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='pixinsight_svg_annotation_hd',
            field=models.ImageField(blank=True, null=True, upload_to='pixinsight-solutions-hd'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='pixinsight_svg_annotation_regular',
            field=models.ImageField(blank=True, null=True, upload_to='pixinsight-solutions-regular'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='skyplot_zoom1',
            field=models.ImageField(blank=True, null=True, upload_to='images/skyplots'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='status',
            field=models.PositiveIntegerField(
                choices=[(0, 'Missing'), (1, 'Basic pending'), (2, 'Basic failed'), (3, 'Basic success'),
                         (4, 'Advanced pending'), (5, 'Advanced failed'), (6, 'Advanced success')], default=0),
        ),
    ]
