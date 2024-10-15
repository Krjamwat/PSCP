# myapp/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    anonymous_user_name = forms.CharField(required=False, label='Your Name')  # Add name field for anonymous users

    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time', 'anonymous_user_name']
