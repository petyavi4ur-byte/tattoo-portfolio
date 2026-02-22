from django.contrib import admin
from .models import ArtistProfile, TattooStyle, CalibrationWork, Sketch, BodyPart, Booking, TimeSlot

admin.site.register(ArtistProfile)
admin.site.register(TattooStyle)
admin.site.register(CalibrationWork)
admin.site.register(Sketch)
admin.site.register(BodyPart)
admin.site.register(Booking)
admin.site.register(TimeSlot)

