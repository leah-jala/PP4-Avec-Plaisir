from django.contrib import admin
from .models import Reservation, Table


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    """ Class to view Reservations on admin panel """
    list_display = (
        'reservation_date',
        'reservation_time',
        'booked_table',
        'guest_name',
        'number_guests',
        'special_requests',
        'last_updated',
    )

    search_fields = ['guest_name', ]

    list_filter = (
        'guest_name',
        'reservation_date',
        'reservation_time',
        'last_updated',
    )


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Class to view Tables on admin panel """
    list_display = (
        'table_id',
        'table_size',
        'minimum',
        'maximum',
    )
    list_filter = ('table_size', 'maximum')
