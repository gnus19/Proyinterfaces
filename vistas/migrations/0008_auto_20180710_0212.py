# Generated by Django 2.0.5 on 2018-07-10 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistas', '0007_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='area',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
