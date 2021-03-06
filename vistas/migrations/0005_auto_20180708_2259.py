# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-08 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistas', '0004_auto_20180708_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='medico',
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vistas.Medico'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='cita',
            name='representante',
        ),
        migrations.AddField(
            model_name='cita',
            name='representante',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vistas.Representante'),
            preserve_default=False,
        ),
    ]
