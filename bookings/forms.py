from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['destination', 'date', 'num_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
