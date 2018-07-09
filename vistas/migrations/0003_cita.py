# Generated by Django 2.0.6 on 2018-07-08 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistas', '0002_auto_20180708_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('medico', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='vistas.Medico')),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=6)),
                ('representante', models.ManyToManyField(blank=True, to='vistas.Representante')),
            ],
        ),
    ]
