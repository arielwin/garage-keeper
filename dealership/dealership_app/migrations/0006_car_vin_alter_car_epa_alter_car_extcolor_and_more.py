# Generated by Django 5.1.1 on 2024-09-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_app', '0005_car_drivetrain_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vin',
            field=models.CharField(default=1, max_length=25, verbose_name='VIN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='epa',
            field=models.IntegerField(verbose_name='MPG'),
        ),
        migrations.AlterField(
            model_name='car',
            name='extColor',
            field=models.CharField(max_length=25, verbose_name='Exterior Color'),
        ),
        migrations.AlterField(
            model_name='car',
            name='intColor',
            field=models.CharField(max_length=25, verbose_name='Interior Color'),
        ),
        migrations.AlterField(
            model_name='car',
            name='trans',
            field=models.CharField(choices=[('M', 'Manual'), ('A', 'Automatic'), ('C', 'CVT')], max_length=1, verbose_name='Transmission'),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(verbose_name='Service date'),
        ),
        migrations.AlterField(
            model_name='service',
            name='sType',
            field=models.CharField(choices=[('SM', 'Standard Maintenance'), ('WA', 'Wash'), ('BA', 'Battery'), ('AC', 'Air Conditioning'), ('WW', 'Windshield Wieprs'), ('TP', 'Tire Pressure'), ('FS', 'Full Service'), ('AL', 'Wheel Alignment'), ('BI', 'Brake Service'), ('TR', 'Tire Rotation'), ('OC', 'Oil Change'), ('CC', 'Coolant Service'), ('SS', 'Suspension Service'), ('PS', 'Power Steering'), ('TS', 'Transmission Service'), ('ES', 'Engine Service')], default='SM', max_length=2, verbose_name='Service Type'),
        ),
    ]
