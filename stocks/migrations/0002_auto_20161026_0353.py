# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
