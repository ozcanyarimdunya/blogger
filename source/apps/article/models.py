from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils.html import format_html
from filer.fields.image import FilerImageField

from source.apps.common.models import BaseModel

User = get_user_model()


class ArticleManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published=True)


class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    content = models.TextField()
    image = FilerImageField(related_name='article_images', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=155, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    objects = ArticleManager()

    class Meta:
        app_label = 'common'
        ordering = ('-updated',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article:detail', kwargs={'slug': self.slug})

    @property
    def preview(self):
        return format_html("""<a href={} class="viewlink" target="blank">Preview</a>""",
                           reverse_lazy('article:preview', kwargs={'slug': self.slug}))


class Stats(BaseModel):
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    path = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'common'
        ordering = ('-views',)
        verbose_name_plural = 'Stats'

    def __str__(self):
        return self.path
