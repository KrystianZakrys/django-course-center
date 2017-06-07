# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Tutorial, Video, Item_Karuzeli


# Create your views here.
def home_view(request):
    tutoriale = Tutorial.objects.all()
    item_karuzeli = Item_Karuzeli.objects.all()
    context = {
        'tutoriale': tutoriale,
        'karuzela_items': item_karuzeli,
    }
    return render(request, 'Pandas/home.html', context)


def tutorial_details(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    videos = Video.objects.filter(tutorial_id = tutorial.id)
    liczba_odcinkow = videos.count()
    if not tutorial.haslo is None and not tutorial.haslo == '':
        context = {
            'tutorial': None,
            'videos': None,
            'liczba_odcinkow': None,
        }
        return render(request, 'Pandas/tutorial_details.html', context)
    else:
        context = {
            'tutorial': tutorial,
            'videos': videos,
            'liczba_odcinkow': liczba_odcinkow,
        }
        return render(request, 'Pandas/tutorial_details.html', context)
