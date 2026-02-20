from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.artist_detail,name='artist_detail'),
    path('catalog/',views.catalog, name='catalog'),
    path('sketch/<int:pk>/',views.sketch_detail, name='sketch_detail'),

]

