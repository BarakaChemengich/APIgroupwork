from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'list.html', {'items': bookings, 'type': 'booking'})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Booking'})

def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'form.html', {'form': form, 'title': 'Edit Booking'})

def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'confirm_delete.html', {'item': booking, 'type': 'booking'})

from django.shortcuts import render

def home(request):
    return render(request, 'list.html')  # or another template for home
