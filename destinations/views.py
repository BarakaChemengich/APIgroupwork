from django.shortcuts import render
from .models import Destination

def home(request):
    return render(request, 'destinations/home.html')

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination.html', {'destinations': destinations})

