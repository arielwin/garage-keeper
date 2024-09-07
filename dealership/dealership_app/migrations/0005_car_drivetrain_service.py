# Generated by Django 5.1.1 on 2024-09-05 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership_app', '0004_remove_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(choices=[('4', 'Four Wheel Drive'), ('A', 'All Wheel Drive'), ('F', 'Front Wheel Drive'), ('R', 'Rear Wheel Drive')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sType', models.CharField(choices=[('SM', 'Standard Maintenance'), ('WA', 'Wash'), ('BA', 'Battery'), ('AC', 'Air Conditioning'), ('WW', 'Windshield Wieprs'), ('TP', 'Tire Pressure'), ('FS', 'Full Service'), ('AL', 'Wheel Alignment'), ('BI', 'Brake Service'), ('TR', 'Tire Rotation'), ('OC', 'Oil Change'), ('CC', 'Coolant Service'), ('SS', 'Suspension Service'), ('PS', 'Power Steering'), ('TS', 'Transmission Service'), ('ES', 'Engine Service')], default='SM', max_length=2)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership_app.car')),
            ],
        ),
    ]