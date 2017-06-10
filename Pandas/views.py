# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Tutorial, Video, Item_Karuzeli,Album,Photo


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
    videos = Video.objects.filter(tutorial_id=tutorial.id)
    allEpisodesCount = videos.count()
    if not tutorial.password is None and not tutorial.password == '':
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
            'allEpisodesCount': allEpisodesCount,
        }
        return render(request, 'Pandas/tutorial_details.html', context)


from forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    f = ContactForm
    # new logic!
    if request.method == 'POST':
        form = f(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            send_mail(contact_name, form_content, contact_email, ['grysiopw@gmail.com'], fail_silently=False)
            message = "Thanks for your message! We will never read it anyway! ;) "
            context = {
                'form': f,
                'message': message,
                'success': True,
            }
            return render(request, 'Pandas/contact.html', context)
        else:
            message = "Something went wrong! :/ "
            context = {
                'form': f,
                'message': message,
                'success': False,
            }
            return render(request, 'Pandas/contact.html', context)
    context = {
        'form': f,
        'message': None,
    }
    return render(request, 'Pandas/contact.html', context)

def about(request):
    return render(request, 'Pandas/about.html')

def gallery(request):
    albums = Album.objects.all()
    context = {
        'albums' : albums,
    }
    return render(request, 'Pandas/gallery.html', context)