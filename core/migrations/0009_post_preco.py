# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-15 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_post_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preco',
            field=models.FloatField(default=0),
        ),
    ]