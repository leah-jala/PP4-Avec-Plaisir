from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime

booking_times = (
            (1, "10:00"), (2, "10:30"), (3, "11:00"),
            (4, "11:30"), (5, "12:00"), (6, "12:30"),
            (7, "13:00"), (8, "13:30"), (9, "14:00"),
            (10, "17:00"), (11, "17:30"), (12, "18:00"),
            (13, "18:30"), (14, "19:00"), (15, "19:30"),
        )


class CreateReservationView(SuccessMessageMixin, CreateView):
    """
    Renders a view to allows the user to create a reservation.
    """
    template_name = 'bookings/bookings.html'
    form_class = ReservationForm
    success_message = "Your reservation was successfully submitted."
    success_url = reverse_lazy('view_reservations')

    def form_valid(self, form):
        """
        Filters existing reservations by date, time and table,
        strikes them off the available tables list and then
        chooses the first available tables.
        """
        form.instance.user = self.request.user
        form.instance.guest_name = form.cleaned_data['guest_name']
        form.instance.phone = form.cleaned_data['phone']
        form.instance.reservation_date = form.cleaned_data['reservation_date']
        form.instance.reservation_time = form.cleaned_data['reservation_time']
        form.instance.number_guests = form.cleaned_data['number_guests']
        form.instance.special_requests = form.cleaned_data['special_requests']

        # Convert the reservation date and time string fields to datetime
        time = form.instance.reservation_time
        for time in booking_times:
            if time == booking_times[0]:
                converted_time = time[1]

        reservation_datetime = datetime.strptime(
            f"{form.instance.reservation_date} {converted_time}",
            '%m/%d/%Y %H:%M')

        # Compare the reservation datetime to the current datetime
        if reservation_datetime < datetime.now():
            form.add_error('reservation_date',
                           'Reservation date and time must be in the future.')
            return self.form_invalid(form)

        # Filter the Reservations table for tables already booked at desired
        # time.
        already_booked_tables = Reservation.objects.filter(
            reservation_date=form.instance.reservation_date,
            reservation_time=form.instance.reservation_time
        ).values_list("booked_table", flat=True)

        # Filter and create a list of the Tables table for the table ids of
        # tables of the right size
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
            messages.error(
                self.request,
                "No tables are available for the selected date and time.")
            return super(CreateReservationView, self).form_invalid(form)


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
        return Reservation.objects.filter(
            user=user).order_by("reservation_date")


class EditReservationView(
        SuccessMessageMixin,
        LoginRequiredMixin,
        UserPassesTestMixin,
        UpdateView):

    """
    Allows the user to make changes to their booking.
    """
    model = Reservation
    form_class = ReservationForm
    template_name = "bookings/update_reservation.html"
    success_message = "Your reservation was successfully updated."
    success_url = reverse_lazy('view_reservations')

    def form_valid(self, form):
        """
        Filters existing reservations by date, time and table,
        strikes them off the available tables list and then
        chooses the first available tables.
        """
        form.instance.user = self.request.user
        form.instance.guest_name = form.cleaned_data['guest_name']
        form.instance.phone = form.cleaned_data['phone']
        form.instance.reservation_date = form.cleaned_data['reservation_date']
        form.instance.reservation_time = form.cleaned_data['reservation_time']
        form.instance.number_guests = form.cleaned_data['number_guests']
        form.instance.special_requests = form.cleaned_data['special_requests']

        # Convert the reservation date and time string fields to datetime
        time = form.instance.reservation_time
        for time in booking_times:
            if time == booking_times[0]:
                converted_time = time[1]

        reservation_datetime = datetime.strptime(
            f"{form.instance.reservation_date} {converted_time}",
            '%m/%d/%Y %H:%M')

        # Compare the reservation datetime to the current datetime
        if reservation_datetime < datetime.now():
            form.add_error('reservation_date',
                           'Reservation date and time must be in the future.')
            return self.form_invalid(form)

        # Filter the Reservations table for tables already booked at desired
        # time.
        already_booked_tables = Reservation.objects.filter(
            reservation_date=form.instance.reservation_date,
            reservation_time=form.instance.reservation_time
        ).values_list("booked_table", flat=True)

        # Filter and create a list of the Tables table for the table ids of
        # tables of the right size
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
            return super(EditReservationView, self).form_valid(form)
        else:
            messages.error(
                self.request,
                "No tables are available for the selected date and time.")
            return super(EditReservationView, self).form_invalid(form)

    def test_func(self):
        """
        Ensures the user making the request is the same
        user that made the reservation.
        """
        booking = self.get_object()
        return self.request.user == booking.user


class DeleteReservationView(
        SuccessMessageMixin,
        UserPassesTestMixin,
        LoginRequiredMixin,
        DeleteView):
    """
    This class handles the deletion of reservations.
    """
    model = Reservation
    template_name = 'bookings/delete_reservation.html'
    success_url = reverse_lazy('view_reservations')
    success_message = "Reservation was successfully deleted."

    def delete(self, request, *args, **kwargs):
        """
        Overrides Django's built-in delete method
        to add a success message.
        """
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        """
        Ensures the user making the request is the same
        user that made the reservation.
        """
        booking = self.get_object()
        return self.request.user == booking.user
