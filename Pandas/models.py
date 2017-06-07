# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone

class Item_Karuzeli(models.Model):
    tytul = models.CharField(max_length=30)
    krotki_opis = models.CharField(max_length=125)
    zdjecie = models.FileField(null=False, blank=False)
    tutorial_link = models.CharField(max_length=125,null=True,blank=True)
    webpage_link = models.CharField(max_length=125,null=True,blank=True)
    aktywny = models.CharField(max_length=25,unique=True,null=True,blank=True)

    def __str__(self):
        return self.tytul

    def __unicode__(self):
        return self.tytul

class Tutorial(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    haslo = models.CharField(max_length=32, blank=True, null=True)
    miniaturka = models.FileField(null = True, blank= True)
    playlista = models.CharField(max_length=100,null = True, blank= True)
    planowana_liczba_odcinkow = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.nazwa

    def __unicode__(self):
        return self.nazwa

class Video(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    tutorial = models.ForeignKey(Tutorial)
    link_youtube = models.CharField(max_length=200)

    def __str__(self):
        return self.tytul

    def __unicode__(self):
       return u"%s/%s" % (self.tytul, self.opis,)


class Tag(models.Model):
    nazwa = models.CharField(max_length=24)

    def __str__(self):
        return self.nazwa

    def __unicode__(self):
        return self.nazwa

class Post(models.Model):
    tytul = models.CharField(max_length=200)
    skrocona_tresc = models.CharField(max_length=350, blank=True)
    tresc = models.TextField(blank=True)
    haslo = models.CharField(max_length=24, blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    '''
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)'''

    def publish(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul

    def __unicode__(self):
        return self.tytul
# class Komentarz(models.Model):
#     data = models.DateField(auto_now=False, auto_now_add=True)
#     id_usera = models.ForeignKey(User, on_delete=models.CASCADE)
#     tresc = models.TextField
