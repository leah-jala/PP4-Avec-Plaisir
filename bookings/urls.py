from bookings.views import CreateReservationView, ViewReservations, EditReservationView, DeleteReservationView
from django.urls import path

urlpatterns = [
    path('bookings/', CreateReservationView.as_view(), name='create_reservation'),
    path('myReservations/', ViewReservations.as_view(), name='view_reservations'),
    path('update/<int:pk>/', EditReservationView.as_view(), name='update_reservation'),
    path('delete/<int:pk>/', DeleteReservationView.as_view(), name='delete_reservation'),
]