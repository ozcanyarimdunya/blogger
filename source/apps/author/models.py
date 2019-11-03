from django.db import models
from django.contrib.auth.models import AbstractUser

from source.apps.common.models import BaseModel


class Author(AbstractUser, BaseModel):
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'common'
