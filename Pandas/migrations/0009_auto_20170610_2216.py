# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pandas', '0008_auto_20170610_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='describtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item_karuzeli',
            old_name='describtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='describtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='describtion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='describtion',
            new_name='description',
        ),
    ]