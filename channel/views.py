from django.shortcuts import render
from .models import Video, Channel, Playlist

# Create your views here.

def index(request):
    videos = Video.objects.all()


    context = {
        'title': 'all videos',
        'videos': videos
    }

    return render(request, 'index.html', context)
