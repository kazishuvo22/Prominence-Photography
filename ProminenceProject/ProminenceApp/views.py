from django.core import serializers
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ProminenceApp.models import *


# Create your views here.

def home(request):
    page = "home"

    general_all = General.objects.all().last()
    about_all = About.objects.all().last()

    context = {
        'all_main_category': PackagesCategory.objects.all(),
        'all_sub_category': SubPackagesCategory.objects.all(),
        'general': general_all,
        'about': about_all
    }
    return render(request, page + ".html", context)


def gallery(request):
    page = "gallery"
    category_name = set()
    gallery_all = Gallery.objects.all()
    for g in gallery_all:
        category_name.add(g.gallery_category.category_name)

    context = {
        'category_name': category_name,
        'gallery_all': gallery_all
    }
    return render(request, page + ".html", context)


def team(request):
    page = "team"
    context = {
        'team_lead': Team.objects.filter(team_category='1'),
        'team_current': Team.objects.filter(team_category='2'),
        'team_former': Team.objects.filter(team_category='3')

    }
    return render(request, page + ".html", context)


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


def contact(request):
    return HttpResponse('Ok')
