from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = (
            'author', 'title', 'subtitle', 'slug', 'image', 'content',
        )


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    readonly_fields = ('slug',)


admin.site.register(Article, ArticleAdmin)
