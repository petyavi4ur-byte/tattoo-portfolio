from django.contrib import admin
from .models import ArtistProfile, TattooStyle, CalibrationWork,Sketch

admin.site.register(ArtistProfile)
admin.site.register(TattooStyle)
admin.site.register(CalibrationWork)
admin.site.register(Sketch)

