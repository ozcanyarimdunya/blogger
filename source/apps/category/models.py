from django.db import models

from source.apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'common'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
