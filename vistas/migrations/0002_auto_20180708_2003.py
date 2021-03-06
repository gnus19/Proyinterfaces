# Generated by Django 2.0.6 on 2018-07-08 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=80)),
                ('porcion', models.CharField(max_length=80)),
                ('alimento', models.CharField(max_length=80)),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='vistas.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='vistas.Usuario')),
                ('representa', models.ManyToManyField(blank=True, to='vistas.Paciente')),
            ],
        ),
        migrations.AlterField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='vistas.Usuario'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='vistas.Usuario'),
        ),
    ]
