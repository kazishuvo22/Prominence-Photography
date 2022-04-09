from django.contrib import admin, messages

# Register your models here.
from django.contrib.auth import get_permission_codename
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import format_html
from django.utils.translation import ngettext

from ProminenceApp.models import General, PackagesCategory, SubPackagesCategory, Packages, Team, Gallery, About, Contact

admin.site.site_header = "Prominence Photography Administration"
admin.site.site_title = "Prominence Photography"


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'last_edited', 'mode', 'last_author', 'image_tag']

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

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 200px; height:100px;" />'.format(obj.hero_image_field.url))

    image_tag.short_description = 'Homepage Image'
    image_tag.allow_tags = True


admin.site.register(General, GeneralAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['short_about', 'last_edited', 'last_author', 'image_tag']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'last_author'):
            obj.last_author = request.user
        obj.save()

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 70px; height:70px;" />'.format(obj.about_body_image.url))

    image_tag.short_description = 'About Body Image'
    image_tag.allow_tags = True


admin.site.register(About, AboutAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'image', 'image_tag']
    list_filter = ['designation']
    ordering = ['-designation']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 70px; height:70px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


admin.site.register(Team, TeamAdmin)


class PackagesAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'main_category', 'sub_category', 'created_at']
    list_filter = ['main_category', 'sub_category']
    ordering = ['main_category']


admin.site.register(Packages, PackagesAdmin)


class PackagesCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created_at', 'image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 70px; height:70px;" />'.format(obj.category_photo.url))

    image_tag.short_description = 'Category Image'
    image_tag.allow_tags = True


admin.site.register(PackagesCategory, PackagesCategoryAdmin)


class SubPackagesCategoryAdmin(admin.ModelAdmin):
    list_display = ['sub_category_name', 'main_category', 'created_at', 'image_tag']
    list_filter = ['main_category']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 70px; height:70px;" />'.format(obj.sub_category_photo.url))

    image_tag.short_description = 'Sub Category Image'
    image_tag.allow_tags = True


admin.site.register(SubPackagesCategory, SubPackagesCategoryAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image_no', 'gallery_category', 'photo', 'image_tag']
    list_filter = ['gallery_category']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.photo.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


admin.site.register(Gallery, GalleryAdmin)


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
