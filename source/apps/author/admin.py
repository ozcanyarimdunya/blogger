from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Author


class AuthorAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Author
        fields = (
            'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
            'image', 'bio', 'groups', 'user_permissions',
        )


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm


admin.site.register(Author, AuthorAdmin)
