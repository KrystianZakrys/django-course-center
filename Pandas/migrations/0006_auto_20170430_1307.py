# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pandas', '0005_auto_20170430_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_karuzeli',
            name='aktywny',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]
