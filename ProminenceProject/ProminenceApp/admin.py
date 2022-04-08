from django.contrib import admin, messages

# Register your models here.
from django.utils.translation import ngettext

from ProminenceApp.models import General, PackagesCategory, SubPackagesCategory, Packages, Team, Gallery, About

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"


class PackagesAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'main_category', 'sub_category']


admin.site.register(Packages, PackagesAdmin)


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'last_edited', 'mode']

    @admin.action(description='Change Mode')
    def mode_button(self, request, queryset):
        if queryset.filter(mode='1'):
            updated_mode = queryset.update(mode='2')
        else:
            updated_mode = queryset.update(mode='1')
        self.message_user(request, ngettext(
            '%d mode was successfully changed',
            '%d mode was successfully changed .',
            updated_mode,
        ) % updated_mode, messages.SUCCESS)

    actions = [mode_button]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(General, GeneralAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['short_about', 'last_edited']


admin.site.register(About, AboutAdmin)
admin.site.register(Team)
admin.site.register(PackagesCategory)
admin.site.register(SubPackagesCategory)

admin.site.register(Gallery)
