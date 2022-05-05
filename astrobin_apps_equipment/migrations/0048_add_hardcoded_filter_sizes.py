# Generated by Django 2.2.24 on 2022-05-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0047_add_planetary_filter_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='other_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Size (mm)'),
        ),
        migrations.AddField(
            model_name='filtereditproposal',
            name='other_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Size (mm)'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='size',
            field=models.CharField(blank=True,
                choices=[('ROUND_1_25_IN', 'Round 1.25"'), ('ROUND_2_IN', 'Round 2"'), ('ROUND_31_MM', 'Round 31 mm'),
                         ('ROUND_36_MM', 'Round 36 mm"'), ('ROUND_50_MM', 'Round 50 mm"'),
                         ('SQUARE_50_MM', 'Square 50x50 mm"'), ('SQUARE_65_MM', 'Square 65x65 mm'),
                         ('EOS_APC_C', 'EOS APC C'), ('EOS_FULL', 'EOS Full'), ('EOS_R', 'EOS R'), ('SONY', 'Sony'),
                         ('T_THREAD_CELL_M42', 'T-thread cell (M42 x 0.75)'), ('SC_CELL', 'SC-cell'),
                         ('OTHER', 'Other')], max_length=32, null=True, verbose_name='Size'
            ),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='size',
            field=models.CharField(blank=True,
                choices=[('ROUND_1_25_IN', 'Round 1.25"'), ('ROUND_2_IN', 'Round 2"'), ('ROUND_31_MM', 'Round 31 mm'),
                         ('ROUND_36_MM', 'Round 36 mm"'), ('ROUND_50_MM', 'Round 50 mm"'),
                         ('SQUARE_50_MM', 'Square 50x50 mm"'), ('SQUARE_65_MM', 'Square 65x65 mm'),
                         ('EOS_APC_C', 'EOS APC C'), ('EOS_FULL', 'EOS Full'), ('EOS_R', 'EOS R'), ('SONY', 'Sony'),
                         ('T_THREAD_CELL_M42', 'T-thread cell (M42 x 0.75)'), ('SC_CELL', 'SC-cell'),
                         ('OTHER', 'Other')], max_length=32, null=True, verbose_name='Size'
            ),
        ),
    ]