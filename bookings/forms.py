from .models import Reservation, Table
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('guest_name', 
                'phone', 
                'reservation_date',
                'reservation_time', 
                'number_guests', 
                'special_requests',)