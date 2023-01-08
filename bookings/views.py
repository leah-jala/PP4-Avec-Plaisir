from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from .models import Reservation, Table

from django.shortcuts import render


def get_booking_page(request):
    return render(request, "bookings/bookings.html")