from django.urls import path
from menus.views import get_menus

urlpatterns = [
        path('menus/', get_menus, name="menus"),
]