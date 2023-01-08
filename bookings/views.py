from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from .models import Reservation, Table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .forms import ReservationForm

def get_booking_page(request):
    return render(
        request, 
        "bookings/bookings.html", 
        {'user': request.user, 'reservation_form': ReservationForm()},
    )

def save_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ReservationForm()
        return render(request, 'bookings/bookings.html', {'form': form})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('guest_name', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
            ),
            'reservation_date',
            'reservation_time',
            'number_guests',
            'special_requests',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
