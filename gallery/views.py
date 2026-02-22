from django.db.models.fields import return_None
from django.shortcuts import render, get_object_or_404,redirect
from .models import Sketch
from django.http import HttpResponse
from .models import ArtistProfile
from .models import BodyPart
from .models import TimeSlot
from datetime import date
from .models import Booking

def catalog(request):
    sketches = Sketch.objects.all()
    return render(request, 'gallery/catalog.html', {'sketches': sketches})

def sketch_detail(request, pk):
    sketch = get_object_or_404(Sketch, pk=pk)
    body_parts = BodyPart.objects.all()
    available_slots = TimeSlot.objects.filter(artist=sketch.artist,
                                              is_booked=False,
                                              date__gte=date.today())
    return render(request, 'gallery/sketch_detail.html', {
        'sketch': sketch,
        'body_parts': body_parts,
        'available_slots': available_slots
    })

def artist_detail(request):
    artist = ArtistProfile.objects.first()
    if artist:
        artist.update_base_rate()
    return render(request, 'gallery/artist_detail.html', {'artist': artist})

def create_booking(request,pk):
    if request.method == 'POST':
        sketch = get_object_or_404(Sketch, pk=pk)
        slot_id = request.POST.get('slot_id')
        slot = get_object_or_404(TimeSlot, id=slot_id)
        Booking.objects.create(sketch=sketch,
                            slot=slot,
                            customer=request.POST.get('client_name'),
                            customer_phone=request.POST.get('client_phone'),
                            final_price=request.POST.get('final_price_hidden'),
                            calculated_size=f"{request.POST.get('width')}*{request.POST.get('height')}",
                            )
        slot.is_booked = True
        slot.save()
        return render(request,'gallery/success.html')
    return redirect('sketch_detail',pk=pk)


