from django.shortcuts import render


# Create your views here.

def home(request):
    page = "home"
    return render(request, page + ".html")


def gallery(request):
    page = "gallery"
    return render(request, page + ".html")


def team(request):
    page = "team"
    return render(request, page + ".html")


def packages(request):
    page = "packages"
    return render(request, page + ".html")
