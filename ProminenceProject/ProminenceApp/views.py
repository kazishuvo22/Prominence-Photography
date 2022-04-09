from django.contrib import messages

from django.core import serializers
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ProminenceApp.models import *


# Create your views here.

def home(request):
    page = "home"
    if General.objects.filter(mode='1').exists():
        general_all = General.objects.all().last()
        about_all = About.objects.all().last()

        context = {
            'all_main_category': PackagesCategory.objects.all(),
            'all_sub_category': SubPackagesCategory.objects.all(),
            'general': general_all,
            'about': about_all
        }
        request.session['facebook_link'] = context['general'].facebook_link
        request.session['instagram_link'] = context['general'].instagram_link
        request.session['whatsapp_link'] = context['general'].whatsapp_link
        request.session['youtube_link'] = context['general'].youtube_link
        request.session['linkedin_link'] = context['general'].linkedin_link
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def gallery(request):
    page = "gallery"
    if General.objects.filter(mode='1').exists():
        category_name = set()
        gallery_all = Gallery.objects.all()
        for g in gallery_all:
            category_name.add(g.gallery_category.category_name)

        context = {
            'category_name': category_name,
            'gallery_all': gallery_all
        }
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def team(request):
    page = "team"
    if General.objects.filter(mode='1').exists():
        context = {
            'team_lead': Team.objects.filter(team_category='1'),
            'team_current': Team.objects.filter(team_category='2'),
            'team_former': Team.objects.filter(team_category='3')

        }
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def packages(request, sub_id):
    page = "packages"
    if General.objects.filter(mode='1').exists():
        context = {
            'all_packages': Packages.objects.filter(sub_category=sub_id)
        }
        print(context['all_packages'])
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def packages_category(request):
    page = "packages_category"
    if General.objects.filter(mode='1').exists():
        context = {
            'category_all': PackagesCategory.objects.all()

        }
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def packages_sub_category(request, category_id):
    page = "packages_sub_category"
    if General.objects.filter(mode='1').exists():
        context = {
            'main_category_name': SubPackagesCategory.objects.filter(main_category=category_id).last(),
            'all_sub_category': SubPackagesCategory.objects.filter(main_category=category_id)
        }
        return render(request, page + ".html", context)
    else:
        return render(request, "missing_general.html")


def contact(request):
    if General.objects.filter(mode='1').exists():
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']

            create_contact = Contact.objects.create(name=name, phone=phone, subject=subject, message=message,
                                                    status="Pending")
            messages.success(request, "Your message has been sent. We will contact you soon.")

        return redirect('home')
    else:
        return render(request, "missing_general.html")
