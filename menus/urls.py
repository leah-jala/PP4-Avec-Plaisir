from django.urls import path
from menus.views import get_menus, get_breakfast_menu, get_lunch_menu, get_dinner_menu

urlpatterns = [
        path('menus/', get_menus, name="menus"),
        path('menus/breakfast', get_breakfast_menu, name="breakfast"),
        path('menus/lunch', get_lunch_menu, name="lunch"),
        path('menus/dinner', get_dinner_menu, name="dinner"),
]