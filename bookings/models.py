from django.db import models
from django.contrib.auth.models import User


TABLE_SIZE = ((2, "2"), (4, "4"), (6, "6"), (8, "8"))
BOOKING_TIMES = (
    (1, "10:00"), (2, "10:30"), (3, "11:00"),
    (4, "11:30"), (5, "12:00"), (6, "12:30"),
    (7, "13:00"), (8, "13:30"), (9, "14:00"),
    (10, "17:00"), (11, "17:30"),(12, "18:00"),
    (13, "18:30"), (14, "19:00"),(15, "19:30"),
)

class Table(models.Model):
    table_id = models.IntegerField(unique=True)
    table_size = models.IntegerField(choices=TABLE_SIZE, default=2)
    minimum = models.IntegerField()
    maximum = models.IntegerField()

    class Meta:
        ordering = ['table_id']

    def __str__(self):
        return str(self.table_id)


class Reservation(models.Model):
    """ Model to create a booking form """
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="guest_reservation"
    )
    guest_name = models.CharField(max_length=25)
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices=BOOKING_TIMES, default=1)
    number_guests = models.IntegerField()
    booked_table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="booked_table")
    special_requests = models.TextField()

    class Meta:
        ordering = ["reservation_date", "reservation_time", "booked_table"]

    def __str__(self):
        return str(self.pk)