from django.shortcuts import render


def get_homepage(request):
    return render(request, "home/base.html")
