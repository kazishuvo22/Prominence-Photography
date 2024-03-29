from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from ProminenceApp import views
from ProminenceProject import settings

urlpatterns = [
                  path('', views.home, name="home"),
                  path('gallery/', views.gallery, name="gallery"),
                  path('team/', views.team, name="team"),
                  path('packages/<str:sub_id>/', views.packages, name="packages"),
                  path('packages_category/', views.packages_category, name="packages_category"),
                  path('packages_sub_category/<str:category_id>/', views.packages_sub_category,
                       name="packages_sub_category"),
                  path('contact/', views.contact, name='contact'),
                  path('terms/', views.terms, name='terms'),
                  path('ads.txt/', views.adstxt, name='adstxt'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
