from django.db import models

from source.apps.common.models import BaseModel
from source.apps.category.models import Category


class Article(BaseModel):
    # todo: add slug field
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        app_label = 'common'

    def __str__(self):
        return self.title
