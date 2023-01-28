from django.urls import path
from home.views import get_homepage

urlpatterns = [
    path('', get_homepage, name="homepage"),
]
