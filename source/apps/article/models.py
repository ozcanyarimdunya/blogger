from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

from source.apps.common.models import BaseModel

User = get_user_model()


class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(max_length=155, null=True, blank=True)

    class Meta:
        app_label = 'common'

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article:detail', kwargs={'slug': self.slug})
