from django.shortcuts import render
from .models import Album

# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    return render(request, 'music/index.html', context)


def details(request, album_id):
    album = Album.objects.get(pk=album_id)
    context = {'album': album, }
    return render(request, 'music/details.html', context)
