from django.core import serializers
from django.core.cache import cache
from django.shortcuts import render
from ProminenceApp.models import *


# Create your views here.

def home(request):
    page = "home"

    context = {
        'all_main_category': PackagesCategory.objects.all(),
        'all_sub_category': SubPackagesCategory.objects.all()
    }
    return render(request, page + ".html", context)


def gallery(request):
    page = "gallery"
    return render(request, page + ".html")


def team(request):
    page = "team"
    return render(request, page + ".html")


def packages(request, sub_id):
    page = "packages"
    context = {
        'all_packages': Packages.objects.filter(sub_category=sub_id)
    }
    print(context['all_packages'])
    return render(request, page + ".html", context)


def packages_category(request):
    page = "packages_category"
    context = {
        'category_all': PackagesCategory.objects.all()

    }
    return render(request, page + ".html", context)


def packages_sub_category(request, category_id):
    page = "packages_sub_category"
    context = {
        'main_category_name': SubPackagesCategory.objects.filter(main_category=category_id).last(),
        'all_sub_category': SubPackagesCategory.objects.filter(main_category=category_id)
    }
    return render(request, page + ".html", context)
