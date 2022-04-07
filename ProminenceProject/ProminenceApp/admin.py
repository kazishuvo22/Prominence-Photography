from django.contrib import admin

# Register your models here.


from ProminenceApp.models import General, PackagesCategory, SubPackagesCategory, Packages, Team, Gallery

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"


class PackagesAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'main_category', 'sub_category']


admin.site.register(General)
admin.site.register(Team)
admin.site.register(PackagesCategory)
admin.site.register(SubPackagesCategory)
admin.site.register(Packages, PackagesAdmin)

admin.site.register(Gallery)

