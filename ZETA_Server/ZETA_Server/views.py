from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "home.html")


def photoes(request):
    return render(request, "home.html")


def recruit(request):
    return render(request, "home.html")
