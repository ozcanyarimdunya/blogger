from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Contact, Stats


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message_', 'email', 'ip', 'is_read',)
    list_display_links = ('name', 'message_')
    list_filter = ('is_read',)
    actions = ('mark_read', 'mark_unread')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        obj.is_read = True
        obj.save()
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    def mark_unread(self, request, queryset):
        queryset.update(is_read=False)

    mark_read.short_description = "Mark selected as read"
    mark_unread.short_description = "Mark selected as unread"


class StatsAdmin(admin.ModelAdmin):
    list_display = ('visit', 'path', 'views', 'last_viewed')
    list_display_links = ('path',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactAdmin)
admin.site.register(Stats, StatsAdmin)
