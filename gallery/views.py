from django.shortcuts import render, get_object_or_404
from .models import Sketch
from django.http import HttpResponse
from .models import ArtistProfile

def catalog(request):
    sketches = Sketch.objects.all()
    return render(request, 'gallery/catalog.html', {'sketches': sketches})

def sketch_detail(request, pk):
    sketch = get_object_or_404(Sketch, pk=pk)
    return render(request, 'gallery/sketch_detail.html', {'sketch': sketch})

def artist_detail(request):
    artist = ArtistProfile.objects.first()
    if artist:
        artist.update_base_rate()
    return render(request, 'gallery/artist_detail.html', {'artist': artist})

