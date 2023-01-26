from . import views
from django.urls import path

urlpatterns = [
    path(
        'bookings/',
        views.CreateReservationView.as_view(),
        name='create_reservation'),
    path(
        'myReservations/',
        views.ViewReservations.as_view(),
        name='view_reservations'),
    path(
        'update/<int:pk>/',
        views.EditReservationView.as_view(),
        name='update_reservation'),
    path(
        'delete/<int:pk>/',
        views.DeleteReservationView.as_view(),
        name='delete_reservation'),
]
