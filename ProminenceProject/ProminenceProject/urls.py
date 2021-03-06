"""ProminenceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap

from ProminenceApp.sitemaps import *
from django.contrib.sitemaps import GenericSitemap

sitemaps = {
    'general': General_Sitemap(),
    'about': About_Sitemap(),
    'team': Team_Sitemap(),
    'packages': Packages_Sitemap(),
    'category': PackagesCategory_Sitemap(),
    'sub_category': SubPackagesCategory_Sitemap(),
}

urlpatterns = [
                  path('myportal/', admin.site.urls),
                  path('', include('ProminenceApp.urls')),
                  path('tinymce/', include('tinymce.urls')),
                  url(r'^chaining/', include('smart_selects.urls')),
                  url(r'^media/(?P<path>.*)$', serve,
                      {'document_root': settings.MEDIA_ROOT}),
                  url(r'^statics/(?P<path>.*)$', serve,
                      {'document_root': settings.STATIC_ROOT}),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
