from django.shortcuts import render


def get_menus(request):
    return render(request, "menus/menus.html")


def get_breakfast_menu(request):
    return render(request, "menus/breakfast.html")


def get_lunch_menu(request):
    return render(request, "menus/lunch.html")


def get_dinner_menu(request):
    return render(request, "menus/dinner.html")
