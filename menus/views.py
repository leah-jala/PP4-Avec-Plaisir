from django.shortcuts import render

def get_menus(request):
    return render(request, "menus/menus.html")
