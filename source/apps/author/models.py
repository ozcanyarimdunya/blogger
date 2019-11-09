from django.db import models
from django.contrib.auth.models import AbstractUser
from filer.fields.image import FilerImageField

from source.apps.common.models import BaseModel


class Author(AbstractUser, BaseModel):
    image = FilerImageField(related_name='author_images', on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'common'
