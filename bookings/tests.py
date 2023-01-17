from django.test import TestCase
from .models import Reservation, Table
from django.contrib.auth import get_user_model
from . import views

class CreateReservationViewTest(TestCase):
    def setUp(self):
        pass  


# Documentation: https://docs.djangoproject.com/en/4.1/topics/testing/overview/