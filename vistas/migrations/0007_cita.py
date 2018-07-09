# Generated by Django 2.0.6 on 2018-07-08 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistas', '0006_auto_20180708_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=6)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vistas.Medico')),
                ('representante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vistas.Representante')),
            ],
        ),
    ]
