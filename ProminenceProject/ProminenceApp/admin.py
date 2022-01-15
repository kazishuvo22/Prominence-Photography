from django.contrib import admin

# Register your models here.
from ProminenceApp.models import General

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"

admin.site.register(General)
