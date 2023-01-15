from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView
from .models import Reservation, Table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .forms import ReservationForm


class CreateReservationView(SuccessMessageMixin, CreateView):
    """
    Renders a view to allows the user to create a reservation.
    """
    template_name = 'bookings/bookings.html'
    form_class = ReservationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.guest_name = form.cleaned_data['guest_name']
        form.instance.phone = form.cleaned_data['phone']
        form.instance.reservation_date = form.cleaned_data['reservation_date']
        form.instance.reservation_time = form.cleaned_data['reservation_time']
        form.instance.number_guests = form.cleaned_data['number_guests']
        form.instance.special_requests = form.cleaned_data['special_requests']
        form.instance.booked_table_id = Table.objects.first().pk  # temporarily get tables from database
        self.object = form.save()
        return super(CreateReservationView, self).form_valid(form)
    
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Your reservation was successfully submitted."


class ViewReservations(LoginRequiredMixin, ListView):
    """
    Allows the user to view their bookings.
    """
    model = Reservation
    template_name = 'bookings/myReservations.html'
    context_object_name = 'reservations'
    ordering = ["-reservation_date"]

    def get_queryset(self):
        """
        Filters out the user's reservations
        """
        user = self.request.user
        return Reservation.objects.filter(user=user).order_by("-reservation_date")