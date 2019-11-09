# Generated by Django 2.2.7 on 2019-11-09 12:26

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='article_images', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_images', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
