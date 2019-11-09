from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, Stats


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = ('is_published', 'author', 'title', 'subtitle', 'slug', 'image', 'content',)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('preview', 'title', 'author', 'created', 'updated', 'is_published')
    readonly_fields = ('slug',)
    list_filter = ('author', 'is_published')
    actions = ('make_publish', 'make_draft')

    def make_publish(self, request, queryset):
        queryset.update(is_published=True)

    def make_draft(self, request, queryset):
        queryset.update(is_published=False)

    make_publish.short_description = "Mark selected as published"
    make_draft.short_description = "Mark selected as draft"


class StatsAdmin(admin.ModelAdmin):
    list_display = ('path', 'views', 'created', 'updated')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Article, ArticleAdmin)
admin.site.register(Stats, StatsAdmin)
