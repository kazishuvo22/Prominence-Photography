from django.contrib import admin, messages

# Register your models here.
from django.contrib.auth import get_permission_codename
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.translation import ngettext

from ProminenceApp.models import General, PackagesCategory, SubPackagesCategory, Packages, Team, Gallery, About, Contact

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"


class PackagesAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'main_category', 'sub_category', 'created_at']
    list_filter = ['main_category', 'sub_category']
    ordering = ['main_category']


admin.site.register(Packages, PackagesAdmin)


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'last_edited', 'mode', 'last_author']

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

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'last_author'):
            obj.last_author = request.user
        obj.save()


admin.site.register(General, GeneralAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['short_about', 'last_edited', 'last_author']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'last_author'):
            obj.last_author = request.user
        obj.save()


admin.site.register(About, AboutAdmin)
admin.site.register(Team)
admin.site.register(PackagesCategory)
admin.site.register(SubPackagesCategory)

admin.site.register(Gallery)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message_time', 'status']
    list_filter = ['phone', 'status']
    search_fields = ['name', 'phone']

    @admin.action(description='Change Status', permissions=['status'])
    def status_button(self, request, queryset):
        if queryset.filter(status='Pending'):
            updated_status = queryset.update(status='Completed')
        else:
            updated_status = queryset.update(status='Pending')
        self.message_user(request, ngettext(
            '%d service was successfully marked as Completed.',
            '%d services were successfully marked as Completed.',
            updated_status,
        ) % updated_status, messages.SUCCESS)

    def has_status_permission(self, request):
        """Does the user have the Change permission?"""
        opts = self.opts
        codename = get_permission_codename('status', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    actions = [status_button]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('contact/', self.contact_view)
        ]
        return custom_urls + urls

    def contact_view(self, request):
        return HttpResponseRedirect("../")

    @admin.display(description='Message Date & Time')
    def message_time(self, obj):
        return obj.message_time

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactAdmin)
