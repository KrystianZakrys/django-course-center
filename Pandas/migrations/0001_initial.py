# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('haslo', models.CharField(blank=True, max_length=32, null=True)),
                ('miniaturka', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('link_youtube', models.CharField(max_length=200)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pandas.Tutorial')),
            ],
        ),
    ]
