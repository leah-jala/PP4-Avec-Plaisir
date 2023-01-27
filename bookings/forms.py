from django import forms
from .models import Reservation, Table


class ReservationForm(forms.ModelForm):
    """
    Form to create and edit a reservation
    """
    class Meta:
        model = Reservation
        fields = (
            'guest_name',
            'phone',
            'reservation_date',
            'reservation_time',
            'number_guests',
            'special_requests',)

        labels = {
            'guest_name': 'Party Name',
            'phone': 'Telephone',
            'reservation_date': 'Date',
            'reservation_time': 'Time',
            'number_guests': 'Number Of Guests',
            'special_requests': "Special Requests",
        }
        