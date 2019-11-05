from django.db import models


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
        app_label = 'common'
        ordering = ('-updated',)

    def __str__(self):
        return f"{self.name}[{self.is_read}]"

    @property
    def message_(self):
        return self.message[:30] + '...'
