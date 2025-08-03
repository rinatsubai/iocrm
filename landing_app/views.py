from django.shortcuts import render
from iocrm_app.models import *

def home(request):
    artist = Artist.objects.filter(landing=True)
    re = Release.objects.filter(landing=True).order_by("-release_date")
    return render(request, 'landing/home.html', {"artist": artist, "release": re})