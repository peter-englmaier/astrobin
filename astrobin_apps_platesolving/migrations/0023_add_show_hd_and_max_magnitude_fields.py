# Generated by Django 2.2.24 on 2022-06-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_platesolving', '0022_solution_pixinsight_finding_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='platesolvingadvancedsettings',
            name='gcvs_max_magnitude',
            field=models.DecimalField(
                blank=True, decimal_places=2,
                help_text="Only GCVS stars up to this magnitude will be rendered. If left empty, the catalog's default value will be used.",
                max_digits=4, null=True, verbose_name='Max. magnitude'
            ),
        ),
        migrations.AddField(
            model_name='platesolvingadvancedsettings',
            name='hd_max_magnitude',
            field=models.DecimalField(
                blank=True, decimal_places=2,
                help_text="Only HD stars up to this magnitude will be rendered. If left empty, the catalog's default value will be used.",
                max_digits=4, null=True, verbose_name='Max. magnitude'
            ),
        ),
        migrations.AddField(
            model_name='platesolvingadvancedsettings',
            name='show_hd',
            field=models.BooleanField(
                default=True,
                help_text='This catalog uses data from the All-sky Compiled Catalogue of 2.5 million stars (Kharchenko+ 2009), VizieR catalog: I/280B.',
                verbose_name='Show HD stars'
            ),
        ),
        migrations.AddField(
            model_name='platesolvingadvancedsettings',
            name='tycho_2_max_magnitude',
            field=models.DecimalField(
                blank=True, decimal_places=2,
                help_text="Only Tycho-2 stars up to this magnitude will be rendered. If left empty, the catalog's default value will be used.",
                max_digits=4, null=True, verbose_name='Max. magnitude'
            ),
        ),
    ]
