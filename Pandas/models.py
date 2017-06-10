# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone

class Item_Karuzeli(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=125)
    picture = models.FileField(null=False, blank=False)
    tutorial_link = models.CharField(max_length=125,null=True,blank=True)
    webpage_link = models.CharField(max_length=125,null=True,blank=True)
    active = models.CharField(max_length=25,unique=True,null=True,blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    password = models.CharField(max_length=32, blank=True, null=True)
    thumbnail = models.FileField(null = True, blank= True)
    playlist = models.CharField(max_length=100,null = True, blank= True)
    episodes_count = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tutorial = models.ForeignKey(Tutorial)
    youtube_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __unicode__(self):
       return u"%s/%s" % (self.title, self.title,)


class Tag(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350, blank=True)
    content = models.TextField(blank=True)
    password = models.CharField(max_length=24, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    post_thumbnail = models.FileField(null=True, blank=True)
    '''
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)'''

    def publish(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
# class Komentarz(models.Model):
#     data = models.DateField(auto_now=False, auto_now_add=True)
#     id_usera = models.ForeignKey(User, on_delete=models.CASCADE)
#     tresc = models.TextField

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    picture = models.FileField(null=True, blank=True)
    describtion =  models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.describtion

    def __unicode__(self):
        return self.describtion

