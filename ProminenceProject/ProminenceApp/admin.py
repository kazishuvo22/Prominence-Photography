from django.contrib import admin

# Register your models here.
from ProminenceApp.models import General, PackagesCategory, SubPackagesCategory, Packages, Team

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"

admin.site.register(General)
admin.site.register(Team)
admin.site.register(PackagesCategory)
admin.site.register(SubPackagesCategory)
admin.site.register(Packages)
