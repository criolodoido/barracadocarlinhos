# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-05 19:06
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171203_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem_titulo', models.CharField(max_length=200)),
                ('foto', cloudinary.models.CloudinaryField(max_length=255, verbose_name='foto')),
            ],
        ),
    ]
