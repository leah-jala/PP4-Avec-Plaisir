from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime


class CreateReservationView(SuccessMessageMixin, CreateView):
    """
    Renders a view to allows the user to create a reservation.
    """
    template_name = 'bookings/bookings.html'
    form_class = ReservationForm
    success_url = reverse_lazy('view_reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.guest_name = form.cleaned_data['guest_name']
        form.instance.phone = form.cleaned_data['phone']
        form.instance.reservation_date = form.cleaned_data['reservation_date']
        form.instance.reservation_time = form.cleaned_data['reservation_time']
        form.instance.number_guests = form.cleaned_data['number_guests']
        form.instance.special_requests = form.cleaned_data['special_requests']

        converted_time = form.instance.reservation_time[1]

        # # Convert the reservation date and time to datetime
        # reservation_datetime = datetime.strptime(
        #     f"{form.instance.reservation_date} {converted_time}",
        #     '%m-%d-%Y %H:%M')

        # # Compare the reservation datetime to the current datetime
        # if reservation_datetime < datetime.now():
        #     form.add_error(
        #         'reservation_date','Reservation date and time must be in the future.')
        #     return self.form_invalid(form)

        # Filter the Reservations table for tables already booked at desired time.
        already_booked_tables = Reservation.objects.filter(
            reservation_date=form.instance.reservation_date, 
            reservation_time=form.instance.reservation_time
        ).values_list("booked_table", flat=True)

        # Filter and create a list of the Tables table for the table ids of tables of the right size
        available_tables = Table.objects.filter(
            table_size__gte=form.instance.number_guests,
            minimum__lte=form.instance.number_guests,
            maximum__gte=form.instance.number_guests
        ).exclude(
            pk__in=already_booked_tables
        ).values_list("pk", flat=True)

        if available_tables:
            # from what's remaining on the list, pick the first table 
            table_id = available_tables[0]
            table = Table.objects.get(pk=table_id)
            form.instance.booked_table = table
            return super(CreateReservationView, self).form_valid(form)
        else:
            messages.error(self.request, "No tables are available for the selected date and time.")
            return super(CreateReservationView, self).form_invalid(form)

    
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
    ordering = ["reservation_date"]

    def get_queryset(self):
        """
        Filters out the user's reservations
        """
        user = self.request.user
        return Reservation.objects.filter(user=user).order_by("reservation_date")


class EditReservationView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "bookings/update_reservation.html"
    success_url = reverse_lazy('view_reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super(EditReservationView, self).form_valid(form)
        
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Your reservation was successfully updated."

class DeleteReservationView(DeleteView):
    model = Reservation
    template_name = 'bookings/delete_reservation.html'
    success_url = reverse_lazy('view_reservations')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Your reservation has been deleted. We hope to see you soon."