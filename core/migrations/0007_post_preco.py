# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-10 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preco',
            field=models.FloatField(default=0),
        ),
    ]
