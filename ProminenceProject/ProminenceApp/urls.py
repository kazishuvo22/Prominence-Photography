from django.contrib import admin
from django.urls import path

from ProminenceApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('team/', views.team, name="team"),
    path('packages/', views.packages, name="packages"),
]