# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-09 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cupom', '0002_cupom_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupom',
            name='validade',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
