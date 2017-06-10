# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Tutorial, Tag, Video, Item_Karuzeli,Post,Album,Photo

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Item_Karuzeli)
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Photo)