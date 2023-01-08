from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from .models import Reservation, Table
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

