# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20161026_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentorder',
            name='success',
        ),
        migrations.AddField(
            model_name='parentorder',
            name='status',
            field=models.CharField(choices=[(b'P', b'In Progress'), (b'C', b'Completed'), (b'F', b'Failed')], default=b'P', max_length=1),
        ),
    ]