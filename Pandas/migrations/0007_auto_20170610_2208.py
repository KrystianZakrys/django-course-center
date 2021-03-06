# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pandas', '0006_auto_20170430_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('describtion', models.CharField(blank=True, max_length=350)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to=b'')),
                ('describtion', models.CharField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pandas.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('describtion', models.CharField(blank=True, max_length=350)),
                ('content', models.TextField(blank=True)),
                ('password', models.CharField(blank=True, max_length=24)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post_thumbnail', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='opis',
            new_name='describtion',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='planowana_liczba_odcinkow',
            new_name='episodes_count',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='haslo',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='playlista',
            new_name='playlist',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='miniaturka',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='nazwa',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='opis',
            new_name='describtion',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='tytul',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='link_youtube',
            new_name='youtube_link',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='Pandas.Tag'),
        ),
    ]
