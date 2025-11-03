from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/home.html', {'destinations': destinations})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinationForm()
    return render(request, 'destinations/add_destination.html', {'form': form})

# ADD THESE NEW FUNCTIONS
def edit_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinationForm(instance=destination)
    
    return render(request, 'destinations/edit_destination.html', {'form': form, 'destination': destination})

def delete_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    if request.method == 'POST':
        destination.delete()
        return redirect('home')
    return render(request, 'destinations/delete_destination.html', {'destination': destination})