"""avecplaisir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import get_homepage
from bookings.views import CreateReservationView, ViewReservations, editReservationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_homepage, name="homepage"),
    path('accounts/', include('allauth.urls')),
    path('bookings/', CreateReservationView.as_view(), name='create_reservation'),
    path('myReservations/', ViewReservations.as_view(), name='view_reservations'),
    path('update/<int:pk>/', editReservationView.as_view(), name='update_reservation'),
]
