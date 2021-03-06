from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from ProminenceApp.models import General, About, Team, PackagesCategory, SubPackagesCategory, Packages


class General_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return General.objects.all()

    def location(self, obj):
        return '/'

    def lastmod(self, obj):
        return obj.last_edited


class About_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return About.objects.all()

    def location(self, obj):
        return '/#about'

    def lastmod(self, obj):
        return obj.last_edited


class Team_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Team.objects.all()

    def location(self, obj):
        return '/team/'

    def lastmod(self, obj):
        return obj.created_at


class PackagesCategory_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return PackagesCategory.objects.all()

    def location(self, obj):
        return '/packages_category/'

    def lastmod(self, obj):
        return obj.created_at


class SubPackagesCategory_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return SubPackagesCategory.objects.all()

    def location(self, obj):
        return '/packages_category/' + str(obj.id)

    def lastmod(self, obj):
        return obj.created_at


class Packages_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Packages.objects.all()

    def location(self, obj):
        return '/packages/' + str(obj.id)

    def lastmod(self, obj):
        return obj.created_at
