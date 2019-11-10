from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


class BaseModel(models.Model):
    """
    BaseModel
    =========
    A Base TimeStamped model with extras field
    All models will inherit BaseModel
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'common'


class Contact(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return f"{self.name}/{self.is_read}"

    @property
    def message_(self):
        return self.message[:30] + '...'


class Stats(BaseModel):
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    path = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-views',)
        verbose_name_plural = 'Stats'

    def __str__(self):
        return self.path

    @property
    def last_viewed(self):
        return self.updated

    @property
    def visit(self):
        return format_html("""<a href="{}" class="button" target="blank">Link</a>""", self.path)
